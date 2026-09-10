# -*- coding: utf-8 -*-
import io,re,sys
sys.path.insert(0,"_build")
from gen_nav import NAV, rel
CUR="wireframe/webshop-ui.html"
def rd(p): return io.open("_build/"+p,encoding="utf-8").read()
src=io.open("wireframe/payment-user-screens.html",encoding="utf-8").read()
head=src[:src.find("<style>")].replace("<title>통합 결제 페이지 화면정의서</title>","<title>웹샵 화면정의서</title>")
style=re.search(r'<style>[\s\S]*?</style>',src).group(0)
js=[s for s in re.findall(r'<script>[\s\S]*?</script>',src) if "docnav" not in s][0]
js=js.replace('var order = ["s09"];','var order = ["w1","w4","w2","w6","w7","w3","w5"];')
NAVBAR='''
<div class="app">
  <nav class="nav">
    <span class="brand"><b>RAGNAROK PORTAL</b><span>웹샵 화면정의서</span></span>
    <span class="nvg">웹샵</span>
    <button type="button" class="nv on" data-go="w1"><b>01</b><span>웹샵 메인</span></button>
    <button type="button" class="nv" data-go="w4"><b>02</b><span>받을 캐릭터 조건 처리</span></button>
    <button type="button" class="nv" data-go="w2"><b>03</b><span>상품 상세보기</span></button>
    <button type="button" class="nv" data-go="w6"><b>04</b><span>결제 완료</span></button>
    <button type="button" class="nv" data-go="w7"><b>05</b><span>구매내역</span></button>
    <button type="button" class="nv" data-go="w3"><b>06</b><span>활용안</span></button>
    <button type="button" class="nv" data-go="w5"><b>07</b><span>기타사항</span></button>
    <span class="ctl">
      <button type="button" class="desc-btn" id="descBtn" title="D">
        <i>&#9776;</i><span class="lbl-on">디스크립션 접기</span><span class="lbl-off">디스크립션 펴기</span>
      </button>
    </span>
  </nav>
  <div class="stage">
'''
def docnav(cur):
    L=['<div id="docnav">','  <div id="docnav-m">']
    for g,items in NAV:
        L.append('    <div class="g">%s</div>'%g)
        for p,l in items:
            on=' class="on"' if p==cur else ''
            L.append('    <a href="%s"%s>%s</a>'%(rel(cur,p),on,l))
    L+=['  </div>','  <span id="docnav-b">문서 <i>&#9650;</i></span>','</div>','<script>','(function () {',
        "  var n = document.getElementById('docnav'), b = document.getElementById('docnav-b');",
        "  b.addEventListener('click', function (e) { e.stopPropagation(); n.classList.toggle('on'); });",
        "  document.addEventListener('click', function () { n.classList.remove('on'); });",
        "  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') n.classList.remove('on'); });",
        '})();','</script>']
    return rd("_docnav_css.html")+"\n".join(L)+"\n"
out=(head+style+rd("ws2-css.html")+rd("ws2-css2.html")+"\n</head>\n<body>\n"+NAVBAR
     +rd("ws2-w1.html")+rd("ws2-w4.html")+rd("ws2-w2.html")+rd("ws2-w6.html")+rd("ws2-w7.html")+rd("ws2-w3.html")+rd("ws2-w5.html")
     +"\n  </div>\n</div>\n\n"+js+"\n\n"+docnav(CUR)+"</body>\n</html>\n")
io.open("wireframe/webshop-ui.html","w",encoding="utf-8",newline="\n").write(out)
io.open("_build/_wsbuild.txt","w",encoding="utf-8").write("webshop-ui.html %d bytes"%len(out.encode("utf-8")))
