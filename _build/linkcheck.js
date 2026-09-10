const fs=require("fs"), path=require("path");
const root="c:/project/test2/ro-plan";
const files=[];
(function walk(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){if(e.name==="_build"||e.name==="_bak"||e.name.startsWith("_test"))continue;const p=path.join(d,e.name);e.isDirectory()?walk(p):p.endsWith(".html")&&files.push(p);}})(root);
let bad=0, total=0, abs=0;
for(const f of files){
  const h=fs.readFileSync(f,"utf8");
  const dir=path.dirname(f);
  for(const m of h.matchAll(/href="([^"#][^"]*\.html)"/g)){
    const href=m[1];
    if(/^https?:/.test(href)) continue;
    total++;
    if(href.startsWith("/")){abs++;console.log("ABS ",path.relative(root,f),"->",href);continue;}
    const t=path.resolve(dir,href);
    if(!fs.existsSync(t)){bad++;console.log("404 ",path.relative(root,f),"->",href);}
  }
}
console.log("\nhtml files:",files.length,"| internal links:",total,"| absolute:",abs,"| broken:",bad);
