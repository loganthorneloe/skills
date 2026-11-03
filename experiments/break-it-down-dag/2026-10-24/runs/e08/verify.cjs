const {chromium}=require('/Users/loganthorneloe/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path=require('path'); const fs=require('fs');
(async()=>{const browser=await chromium.launch({headless:true,executablePath:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"});const context=await browser.newContext();const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));const root=__dirname;
const results=[];
for(const [name,width,height] of [['desktop',1440,1050],['mobile',390,844]]){
await page.setViewportSize({width,height});await page.goto('file://'+path.join(root,'report.html'));await page.evaluate(()=>document.fonts.ready);
results.push({name,...await page.evaluate(()=>({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.naturalWidth})),controls:document.querySelectorAll('button,input,select').length,externalAssets:document.querySelectorAll('img[src^="http"],link[href^="http"],script[src^="http"]').length}))});
await page.screenshot({path:path.join(root,name+'-top.png')});
await page.getByRole('heading',{name:'3. What the isolation levels rule out'}).scrollIntoViewIfNeeded();await page.screenshot({path:path.join(root,name+'-levels.png')});
await page.getByRole('heading',{name:'4. A stable snapshot can still allow the wrong result'}).scrollIntoViewIfNeeded();await page.screenshot({path:path.join(root,name+'-figure.png')});
await page.locator('.figscroll').screenshot({path:path.join(root,name+'-figure-detail.png')});
await page.locator('figure.wide').screenshot({path:path.join(root,name+'-table-detail.png')});
await page.getByRole('heading',{name:'6. Choose protection that matches the rule'}).scrollIntoViewIfNeeded();await page.screenshot({path:path.join(root,name+'-sql.png')});
}
await page.keyboard.press('Tab');results.push({keyboardFocus:await page.evaluate(()=>({tag:document.activeElement.tagName,outline:getComputedStyle(document.activeElement).outlineStyle}))});
const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});const staticPage=await nojs.newPage();await staticPage.goto('file://'+path.join(root,'report.html'));results.push({staticHeading:await staticPage.locator('h1').textContent(),staticImages:await staticPage.locator('img').count()});
fs.writeFileSync(path.join(root,'verification.json'),JSON.stringify({results,errors},null,2));console.log(JSON.stringify({results,errors},null,2));await browser.close();})();
