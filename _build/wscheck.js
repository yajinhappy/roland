const fs=require("fs");
const f="wireframe/webshop-ui.html";
const h=fs.readFileSync(f,"utf8");
// tag balance
let bad=[];
for(const t of ["div","section","span","button","ul","li","p","table","tr","td","th","svg","b","em","i","style","script","nav","head","body","html"]){
  const o=(h.match(new RegExp("<"+t+"(?:\\s[^>]*)?>","g"))||[]).length;
  const c=(h.match(new RegExp("</"+t+">","g"))||[]).length;
  if(o!==c) bad.push(t+" "+o+"/"+c);
}
console.log("TAG BALANCE:", bad.length?bad.join(", "):"OK");
// screens vs nav vs order
const screens=[...h.matchAll(/<section class="screen[^"]*" id="(\w+)"/g)].map(m=>m[1]);
const nav=[...h.matchAll(/data-go="(\w+)"/g)].map(m=>m[1]);
const order=(h.match(/var order = \[([^\]]*)\]/)||["",""])[1].replace(/["\s]/g,"").split(",").filter(Boolean);
console.log("screens",screens," nav",nav," order",order,
  " 일치:", JSON.stringify(screens)===JSON.stringify(nav) && JSON.stringify(screens)===JSON.stringify(order));
// pins vs desc rows per screen
for(const m of h.matchAll(/<section class="screen[^"]*" id="(\w+)">([\s\S]*?)<\/section>/g)){
  const id=m[1], body=m[2];
  const parts=body.split('<div class="dcol">');
  const pins=[...parts[0].matchAll(/class="mk(?: mk-w)?"[^>]*>([^<]+)</g)].map(x=>x[1].trim());
  const rows=[...(parts[1]||"").matchAll(/class="mk(?: mk-w)?">([^<]+)</g)].map(x=>x[1].trim());
  const up=[...new Set(pins)].sort(), ur=[...new Set(rows)].sort();
  const ok=JSON.stringify(up)===JSON.stringify(ur);
  console.log("  "+id+" pins["+up.join(",")+"] rows["+ur.join(",")+"] "+(ok?"ok":"MISMATCH"));
}
// undefined classes
const css=(h.match(/<style>[\s\S]*?<\/style>/g)||[]).join("\n");
const def=new Set([...css.matchAll(/\.([a-zA-Z][\w-]*)/g)].map(m=>m[1]));
const used=new Set();
for(const m of h.matchAll(/class="([^"]+)"/g)) m[1].split(/\s+/).forEach(c=>c&&used.add(c));
const miss=[...used].filter(c=>!def.has(c));
console.log("미정의 클래스:", miss.length?miss.join(", "):"none");
