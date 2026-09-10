# -*- coding: utf-8 -*-
import io, sys, re
sys.path.insert(0,"_build")
from gen_nav import NAV, rel

DOCNAV_CSS = io.open("_build/_docnav_css.html",encoding="utf-8").read()

def docnav(cur):
    L=['<div id="docnav">','  <div id="docnav-m">']
    for group,items in NAV:
        L.append('    <div class="g">%s</div>'%group)
        for path,label in items:
            on=' class="on"' if path==cur else ''
            L.append('    <a href="%s"%s>%s</a>'%(rel(cur,path),on,label))
    L+=['  </div>','  <span id="docnav-b">문서 <i>&#9650;</i></span>','</div>',
        '<script>','(function () {',
        "  var n = document.getElementById('docnav'), b = document.getElementById('docnav-b');",
        "  b.addEventListener('click', function (e) { e.stopPropagation(); n.classList.toggle('on'); });",
        "  document.addEventListener('click', function () { n.classList.remove('on'); });",
        "  document.addEventListener('keydown', function (e) {",
        "    if (e.key === 'Escape') n.classList.remove('on');",
        '  });','})();','</script>']
    return DOCNAV_CSS + "\n".join(L) + "\n"

def cat(*parts):
    return "".join(io.open("_build/"+p,encoding="utf-8").read() for p in parts)

def emit(out, head, body, cur, spy=True):
    h = cat(head, "_style.html") + body
    if spy: h += cat("_spy.html")
    h += "\n" + docnav(cur) + "</body>\n</html>\n"
    io.open(out,"w",encoding="utf-8",newline="\n").write(h)
    print("%-42s %6d bytes" % (out, len(h.encode("utf-8"))))

# 1) 1-page overview
emit("wiki/planning/payment-overview.html", "head-v2o.html",
     cat("body-v2o.html"), "wiki/planning/payment-overview.html", spy=False)

# 2) main design doc
emit("wiki/planning/payment.html", "head-v2.html",
     cat("body-v2-open.html","body-v2-c1.html","body-v2-c2.html","body-v2-c3.html",
         "body-v2-c4.html","body-v2-review.html","body-v2-close.html"),
     "wiki/planning/payment.html")

# 3) 웹샵/통합결제 구조
emit("wiki/planning/payment-webshop-structure.html", "head-struct.html",
     cat("body-struct.html"), "wiki/planning/payment-webshop-structure.html")

# 4) 웹샵/통합결제 기획
emit("wiki/planning/webshop-payment-prd.html", "head-prd.html",
     cat("prd-exec-css.html", "body-prd.html"), "wiki/planning/webshop-payment-prd.html")
