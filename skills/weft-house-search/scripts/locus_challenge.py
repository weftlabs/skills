#!/usr/bin/env python3
"""Get an unpaid Locus RentCast challenge. Never signs or pays."""
import argparse
import base64
from decimal import Decimal
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid

HOST = "rentcast.x402.paywithlocus.com"
PATHS = {"/rentcast/rental-listings", "/rentcast/rent-estimate"}
USDC_BASE = "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913"

class NoRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("body_json", type=Path)
    args = parser.parse_args()
    parsed = urllib.parse.urlsplit(args.url)
    if (parsed.scheme != "https" or parsed.hostname != HOST or
        parsed.port not in (None, 443) or parsed.username or parsed.password or
        parsed.query or parsed.fragment or parsed.path not in PATHS):
        raise ValueError("URL must be an approved HTTPS RentCast listing or estimate endpoint")
    payload = args.body_json.read_bytes()
    if len(payload) > 65536 or not isinstance(json.loads(payload), dict):
        raise ValueError("Body file must be a JSON object below 64 KiB")
    request = urllib.request.Request(args.url, data=payload, method="POST",
        headers={"Content-Type": "application/json", "Accept": "application/json"})
    opener = urllib.request.build_opener(NoRedirects())
    try:
        with opener.open(request, timeout=30) as response:
            raise ValueError("Expected unpaid HTTP 402, received HTTP " + str(response.status))
    except urllib.error.HTTPError as response:
        if response.code != 402:
            raise ValueError("Expected unpaid HTTP 402, received HTTP " + str(response.code))
        body = json.loads(response.read(65536))
        request_id = str(uuid.UUID(body["requestId"]))
        header_id = response.headers.get("locus-request-id")
        if header_id and str(uuid.UUID(header_id)) != request_id:
            raise ValueError("Locus body/header request IDs do not match")
        encoded = response.headers.get("payment-required")
        if not encoded:
            raise ValueError("Missing payment challenge header")
        challenge = json.loads(base64.b64decode(encoded, validate=True))
    if challenge.get("x402Version") != 2:
        raise ValueError("Unexpected payment protocol version")
    matches = [a for a in challenge.get("accepts", [])
        if a.get("scheme") == "exact" and a.get("network") == "eip155:8453"
        and a.get("asset", "").lower() == USDC_BASE]
    if len(matches) != 1:
        raise ValueError("Expected one exact Base USDC price")
    amount_text = matches[0].get("amount", "")
    if not isinstance(amount_text, str) or not amount_text.isdigit():
        raise ValueError("Invalid micro-USDC price")
    amount = int(amount_text)
    if not 0 < amount <= 50000:
        raise ValueError("Quoted price exceeds the demo per-call cap or is invalid")
    cost = format(Decimal(amount) / Decimal(1000000), ".6f")
    print(json.dumps({
        "http_status": 402,
        "request_id": request_id,
        "quoted_usd": cost,
        "next_fetch": {
            "url": args.url,
            "method": "POST",
            "headers": {"Content-Type": "application/json", "x-locus-request-id": request_id},
            "body": payload.decode("utf-8"),
            "max_cost_usd": cost,
            "idempotency_key": "weft-house-search-" + str(uuid.uuid4())
        },
        "notice": "No payment made. Save this output before one authorized Weft fetch."
    }, indent=2))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Do not print raw responses, payment headers, or payment addresses.
        print("Unpaid challenge failed: " + str(exc), file=sys.stderr)
        sys.exit(1)
