// Capture offline pages; no provider or other network requests are permitted.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
(async () => {
  const directory = path.resolve(process.argv[2]);
  const browser = await chromium.launch({headless: true, executablePath: process.env.CHROMIUM_EXECUTABLE || undefined});
  try {
    const page = await browser.newPage({viewport: {width:1600,height:1000},deviceScaleFactor:1});
    await page.route(/^https?:/, route => route.abort());
    const checks = [];
    for (const file of fs.readdirSync(directory).filter(f => f.endsWith('.html') && f !== 'index.html')) {
      await page.setViewportSize({width:1600,height:1000});
      await page.goto(pathToFileURL(path.join(directory,file)).href);
      await page.evaluate(() => document.fonts.ready);
      const missing = await page.locator('img').evaluateAll(imgs => imgs.filter(i=>!i.complete||!i.naturalWidth).length);
      if (missing) throw new Error(`${file}: ${missing} missing logos`);
      await page.screenshot({path:path.join(directory,file.replace('.html','.png')),fullPage:true});
      if (file === 'session.html') {
        fs.copyFileSync(path.join(directory,'session.png'), path.join(directory,'session-full.png'));
        await page.screenshot({path:path.join(directory,'session.png')});
        // A result-only view, with the same heading and provider panel. The HTML
        // and full screenshot retain every visible message in recorded order.
        await page.evaluate(() => {
          const messages = [...document.querySelector('.conversation').children];
          messages.slice(0,-1).forEach(m => m.style.display = 'none');
        });
        await page.screenshot({path:path.join(directory,'session-result.png'),fullPage:true});
        await page.reload();
      }
      await page.setViewportSize({width:390,height:844});
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
      if (overflow) throw new Error(`${file}: mobile page overflow`);
      checks.push({file,missingLogos:missing,mobileOverflow:overflow});
    }
    fs.writeFileSync(path.join(directory,'capture-checks.json'),JSON.stringify(checks,null,2)+'\n');
    console.log(`Captured and checked ${checks.length} examples`);
  } finally { await browser.close(); }
})().catch(error=>{console.error(error.message);process.exitCode=1;});
