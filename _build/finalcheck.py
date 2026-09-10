# -*- coding: utf-8 -*-
import io,re,glob,os
rows=[]
for f in sorted(glob.glob("**/*.html",recursive=True)):
    f=f.replace(os.sep,"/")
    if f.startswith("_build/") or f.startswith("wiki/webshop/"): continue
    h=io.open(f,encoding="utf-8").read()
    bad=[]
    for t in ["div","main","section","span","button","ul","li","p","table","tr","td","th","svg","b","a","style","script"]:
        o=len(re.findall(r"<"+t+r"(?:\s[^>]*)?>",h)); c=len(re.findall(r"</"+t+r">",h))
        if o!=c: bad.append("%s %d/%d"%(t,o,c))
    css="\n".join(re.findall(r"<style>[\s\S]*?</style>",h))
    d=set(re.findall(r"\.([a-zA-Z][\w-]*)",css)); u=set()
    for m in re.findall(r'class="([^"]+)"',h): u.update(m.split())
    miss=sorted(u-d)
    nav=re.search(r'<div id="docnav-m">[\s\S]*?</div>\n',h)
    on=len(re.findall(r'class="on"',nav.group(0))) if nav else -1
    rows.append("%-44s %-14s cls:%-3d nav_on:%d"%(f,("OK" if not bad else ",".join(bad)),len(miss),on))
    if miss: rows.append("      미정의: "+", ".join(miss[:8]))
io.open("_build/final.txt","w",encoding="utf-8").write("\n".join(rows))
