const { chromium }=require('/Users/loganthorneloe/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');const path=require('path');
(async()=>{const dir=__dirname;const browser=await chromium.launch({headless:true,executablePath:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"});const results=[];
for(const [name,width,height] of [['desktop',1280,900],['mobile',390,844]]){
 const context=await browser.newContext({viewport:{width,height},offline:true});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+path.join(dir,'report.html'));await page.evaluate(()=>document.fonts.ready);
 const data=await page.evaluate(()=>({title:document.title,width:innerWidth,scrollWidth:document.documentElement.scrollWidth,images:[...document.images].map(x=>({loaded:x.complete&&x.naturalWidth>0,naturalWidth:x.naturalWidth,width:x.width})),fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),sections:document.querySelectorAll('section').length,interactiveControls:document.querySelectorAll('button,input,select').length,links:[...document.querySelectorAll('a[href]')].filter(x=>!x.getAttribute('href').startsWith('https:')).map(x=>x.getAttribute('href'))}));
 await page.screenshot({path:path.join(dir,name+'.png'),fullPage:true});
 await page.locator('table').first().screenshot({path:path.join(dir,name+'-table.png')});
 await page.locator('pre').screenshot({path:path.join(dir,name+'-code.png')});
 await page.locator('figure').screenshot({path:path.join(dir,name+'-figure.png')});
 results.push({name,...data,errors});await context.close();
}
fs.writeFileSync(path.join(dir,'verification.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));await browser.close();})().catch(e=>{console.error(e);process.exit(1)});
