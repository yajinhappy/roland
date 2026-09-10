const fs=require("fs");
for(const f of ["wireframe/payment-user-screens.html","wireframe/payment-admin-screens.html"]){
  const h=fs.readFileSync("c:/project/test2/ro-plan/"+f,"utf8");
  const ids=[...h.matchAll(/<section class="screen" id="(s\d+)"/g)].map(m=>m[1]);
  const navs=[...h.matchAll(/data-go="(s\d+)"/g)].map(m=>m[1]);
  const ord=(h.match(/var order = \[([^\]]*)\]/)||["",""])[1].replace(/"/g,"");
  console.log("\n== "+f.split("/").pop());
  console.log("  screens ["+ids.join(",")+"]  nav ["+navs.join(",")+"]  order ["+ord+"]");
  const navSet=[...navs].sort().join(","), idSet=[...ids].sort().join(",");
  const ordSet=ord.split(",").sort().join(",");
  console.log("  집합 일치:", navSet===idSet && ordSet===idSet);
  const marker='<div class="dcol">';
  let pinOk=true;
  for(const sec of h.matchAll(/<section class="screen" id="(s\d+)"[\s\S]*?<\/section>/g)){
    const s=sec[0], id=sec[1], i=s.indexOf(marker);
    const pins=[...s.slice(0,i).matchAll(/class="mk"[^>]*>(\d+)</g)].map(m=>m[1]).sort();
    const rows=[...s.slice(i).matchAll(/<span class="mk">(\d+)<\/span>/g)].map(m=>m[1]).sort();
    const ok=JSON.stringify(pins)===JSON.stringify(rows);
    if(!ok) pinOk=false;
    console.log("  "+id+" pins["+pins.join(",")+"] rows["+rows.join(",")+"] "+(ok?"ok":"MISMATCH"));
  }
  let bal=[]; for(const t of ["section","div","table","span","tr","td","th","p","ul","li"]){
    const o=(h.match(new RegExp("<"+t+"[ >]","g"))||[]).length,c=(h.match(new RegExp("</"+t+">","g"))||[]).length;
    if(o!==c)bal.push(t+" "+o+"/"+c);}
  console.log("  태그:", bal.join(",")||"ok", "| 핀:", pinOk?"ok":"NG");
  const css=h.split("</style>")[0];
  const defined=new Set([...css.matchAll(/\.([a-zA-Z][\w-]*)/g)].map(m=>m[1]));
  const body=h.split("</style>").slice(1).join("</style>");
  const used=new Set(); for(const m of body.matchAll(/class="([^"]+)"/g)) m[1].split(/\s+/).forEach(c=>c&&used.add(c));
  console.log("  미정의 클래스:", [...used].filter(c=>!defined.has(c)&&!["pane-pc","pcframe","g"].includes(c)).join(",")||"none");
  const on=(h.match(/<a href="[^"]*" class="on">([^<]*)</)||["",""])[1];
  console.log("  docnav 활성:", on);
}
