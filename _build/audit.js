const fs=require("fs");
const strip=s=>s.replace(/<script[\s\S]*?<\/script>/g,"").replace(/<style[\s\S]*?<\/style>/g,"")
                 .replace(/<svg[\s\S]*?<\/svg>/g,"").replace(/<[^>]+>/g," ").replace(/&[a-z]+;/g," ")
                 .replace(/\s+/g," ").trim();
const files=[
 ["payment.html (새 개요)","wiki/planning/payment.html"],
 ["global-payment.html (상세)","wiki/planning/global-payment.html"],
 ["pg-multi-entity (벤치마킹)","wiki/benchmark/pg-multi-entity.html"],
 ["game-platform (벤치마킹)","wiki/benchmark/game-platform-payment.html"],
 ["user-screens (화면)","wireframe/payment-user-screens.html"],
 ["admin-screens (화면)","wireframe/payment-admin-screens.html"],
];
let tot=0;
console.log("문서".padEnd(30)+"글자".padStart(8)+"문단".padStart(6)+"표".padStart(5)+"그림".padStart(5)+"박스".padStart(6));
console.log("-".repeat(62));
for(const [name,f] of files){
  const h=fs.readFileSync(f,"utf8");
  const txt=strip(h);
  const paras=(h.match(/<p class="dr-b"|<p>|<p [^>]*class="(?!cap|grp)/g)||[]).length;
  const tables=(h.match(/<table[ >]/g)||[]).length;
  const svgs=(h.match(/<svg[ >]/g)||[]).length;
  const boxes=(h.match(/class="(note|spec|imm|warn)[" ]/g)||[]).length;
  tot+=txt.length;
  console.log(name.padEnd(30)+String(txt.length).padStart(8)+String(paras).padStart(6)+String(tables).padStart(5)+String(svgs).padStart(5)+String(boxes).padStart(6));
}
console.log("-".repeat(62));
console.log("합계".padEnd(30)+String(tot).padStart(8)+"  자  ≈ A4 "+Math.round(tot/1600)+"장");

console.log("\n[ payment.html — 장별 ]");
const h=fs.readFileSync("wiki/planning/payment.html","utf8");
const secs=[...h.matchAll(/<section id="(c\d|review)">([\s\S]*?)<\/section>/g)];
for(const m of secs){
  const t=strip(m[2]);
  const paras=(m[2].match(/<p>|<p style/g)||[]).length;
  const notes=(m[2].match(/class="note/g)||[]).length;
  const tables=(m[2].match(/<table[ >]/g)||[]).length;
  const h3=(m[2].match(/<h3>/g)||[]).length;
  console.log(("  "+m[1]).padEnd(12)+String(t.length).padStart(6)+"자  절 "+h3+"  문단 "+paras+"  표 "+tables+"  note "+notes);
}
