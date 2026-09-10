# -*- coding: utf-8 -*-
import io,re,glob
o=[]
for f in ["wiki/planning/global-payment.html","wiki/benchmark/pg-multi-entity.html","wiki/planning/payment.html"]:
    h=io.open(f,encoding="utf-8").read()
    h=re.sub(r'<div id="docnav">[\s\S]*?</div>\n','',h)
    t=re.sub(r'<[^>]+>',' ',h); t=re.sub(r'\s+',' ',t)
    for kw in ["GGU","말레이","Malaysia","GGL","인도네시아","GGH","싱가포르","GGV","홍콩","Oneverse","GOC","JollyMax","PagSeguro","Razer","Xsolla","Airwallex","PayerMax","EBANX","Antom"]:
        for m in re.finditer(re.escape(kw),t):
            s=max(0,m.start()-150); e=min(len(t),m.end()+150)
            o.append("[%s] …%s…"%(kw,t[s:e].strip()))
seen=set(); out=[]
for x in o:
    k=x[:120]
    if k in seen: continue
    seen.add(k); out.append(x)
io.open("_o.txt","w",encoding="utf-8").write("\n".join(out))
