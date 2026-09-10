const fs=require("fs");
const f="c:/project/test2/ro-plan/wireframe/payment-lifecycle-screens.html";
const h=fs.readFileSync(f,"utf8");
const ids=[...h.matchAll(/<section class="screen" id="(s\d+)"/g)].map(m=>m[1]);
const navs=[...h.matchAll(/data-go="(s\d+)"/g)].map(m=>m[1]);
console.log("screens", ids.join(","));
console.log("nav    ", navs.join(","));
console.log("match:", JSON.stringify(ids)===JSON.stringify(navs));
const marker = '<div class="dcol">';
for(const sec of h.matchAll(/<section class="screen" id="(s\d+)"[\s\S]*?<\/section>/g)){
  const s=sec[0], id=sec[1];
  const i=s.indexOf(marker);
  const stage=s.slice(0,i), dcol=s.slice(i);
  const pins=[...stage.matchAll(/class="mk"[^>]*>(\d+)</g)].map(m=>m[1]).sort();
  const rows=[...dcol.matchAll(/<span class="mk">(\d+)<\/span>/g)].map(m=>m[1]).sort();
  const miss=pins.filter(p=>!rows.includes(p));
  const extra=rows.filter(r=>!pins.includes(r));
  const dup=pins.filter((p,k)=>pins.indexOf(p)!==k);
  console.log(id,"pins["+pins.join(",")+"] rows["+rows.join(",")+"]",(miss.length||extra.length||dup.length)?("MISS:"+miss+" EXTRA:"+extra+" DUP:"+dup):"ok");
}
let bal=[]; for(const t of ["section","div","table","span","tr","td","th","p"]){const o=(h.match(new RegExp("<"+t+"[ >]","g"))||[]).length,c=(h.match(new RegExp("</"+t+">","g"))||[]).length;if(o!==c)bal.push(t+" "+o+"/"+c);}
console.log("tag balance:", bal.join(", ")||"ok");
const css=h.split("</style>")[0];
const defined=new Set([...css.matchAll(/\.([a-zA-Z][\w-]*)/g)].map(m=>m[1]));
const body=h.split("</style>").slice(1).join("</style>");
const used=new Set(); for(const m of body.matchAll(/class="([^"]+)"/g)) m[1].split(/\s+/).forEach(c=>c&&used.add(c));
console.log("undefined classes:", [...used].filter(c=>!defined.has(c)).join(", ")||"none");
