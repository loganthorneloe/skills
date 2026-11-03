const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
const {pathToFileURL,fileURLToPath}=require('url');
(async()=>{
  const browser=await chromium.launch({headless:true,...(process.env.BROWSER_EXECUTABLE?{executablePath:process.env.BROWSER_EXECUTABLE}:{})});
  const context=await browser.newContext({viewport:{width:1440,height:1000},offline:true});
  const page=await context.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const base=pathToFileURL(path.join(__dirname,'index.html')).href;
  await page.goto(base);
  const missing=[];
  for(const href of await page.locator('a').evaluateAll(es=>es.map(e=>e.getAttribute('href')))){
    const url=new URL(href,base);
    if(url.protocol==='file:'&&!fs.existsSync(fileURLToPath(url)))missing.push(href);
  }
  const states=[];
  for(const topic of ['evals','causal','encryption','isolation']){
    await page.selectOption('#topic',topic);
    const srcs=await page.locator('iframe').evaluateAll(es=>es.map(e=>e.src));
    for(const src of srcs)if(!fs.existsSync(fileURLToPath(src)))throw Error('Missing iframe report: '+src);
    states.push({topic,srcs:srcs.map(src=>path.relative(__dirname,fileURLToPath(src)))});
  }
  await page.selectOption('#topic','evals');
  const desktop=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));
  await page.screenshot({path:path.join(__dirname,'review-desktop.png')});
  const mobileContext=await browser.newContext({viewport:{width:390,height:844},offline:true});
  const mobilePage=await mobileContext.newPage();
  mobilePage.on('pageerror',e=>errors.push(e.message));
  await mobilePage.goto(base);
  const mobile=await mobilePage.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));
  await mobilePage.screenshot({path:path.join(__dirname,'review-mobile.png')});
  await mobilePage.locator('#topic').focus();
  await mobilePage.locator('#topic').press('c');
  await mobilePage.keyboard.press('Tab');
  const keyboard=await mobilePage.locator('#topic').inputValue();
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844},offline:true});
  const fallback=await nojs.newPage();await fallback.goto(base);
  const staticLinks=await fallback.locator('a[href$="report.html"]').count();
  const result={desktop,mobile,missing,errors,states,keyboard,staticReportLinks:staticLinks};
  fs.writeFileSync(path.join(__dirname,'review-verification.json'),JSON.stringify(result,null,2)+'\n');
  await browser.close();
  if(missing.length||errors.length||desktop.width>desktop.viewport||mobile.width>mobile.viewport||staticLinks!==8||keyboard!=='causal')throw Error(JSON.stringify(result));
  console.log('PASS: desktop/mobile, local links, four topic choices, keyboard operation, and eight static report links.');
})().catch(e=>{console.error(e);process.exit(1)});
