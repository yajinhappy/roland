# -*- coding: utf-8 -*-
import io,re,sys
h=io.open(sys.argv[1],encoding="utf-8").read()
h=re.sub(r'<div id="docnav">[\s\S]*?</div>\n','',h)
t=re.sub(r'<svg[\s\S]*?</svg>','[도식]',h)
t=re.sub(r'<style[\s\S]*?</style>','',t); t=re.sub(r'<script[\s\S]*?</script>','',t)
t=re.sub(r'<(h1|h2|h3|h4|tr|li|p|div|figcaption)\b[^>]*>','\n',t)
t=re.sub(r'<t[dh]\b[^>]*>',' | ',t); t=re.sub(r'<[^>]+>','',t)
for a,b in [('&middot;','·'),('&nbsp;',' '),('&amp;','&'),('&rarr;','→'),('&times;','×')]: t=t.replace(a,b)
t=re.sub(r'&[a-zA-Z#0-9]+;','',t)
io.open("_o.txt","w",encoding="utf-8").write("\n".join(l.strip() for l in t.split("\n") if l.strip()))
