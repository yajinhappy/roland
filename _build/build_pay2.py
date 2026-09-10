# -*- coding: utf-8 -*-
# 라그나로크원페이 화면정의서 — payment-checkout-currency.html 골격 재사용
import io, sys
sys.path.insert(0, "_build")
from gen_nav import NAV, rel

SRC = "wireframe/payment-checkout-currency.html"
OUT = "wireframe/payment-checkout-channels.html"

src = io.open(SRC, encoding="utf-8").read()
head = src[:src.index("</style>")]
head = head.replace("<title>통합결제 화면정의서</title>",
                    "<title>라그나로크원페이 화면정의서</title>")
js = src[src.index("<script>\n(function () {"):src.index("</script>") + len("</script>")]

# ══════════════════ 추가 CSS ══════════════════
CSS = """
  /* ═══════════ 폰트 가이드 ═══════════
     한글 최소      10.5px   — 9px 이하는 자모가 붙어 깨져 보인다
     영문 · 숫자     9px     — mono 기준
     배지 · 태그     8.5px   — 영문 전용일 때만 8px 허용
     자간           한글이 섞이면 0.06em 이하 — 넓은 자간은 한글을 흩어 놓는다
                    영문 전용 코드에만 0.09em 이상 허용
     ═══════════════════════════════════ */

  /* 섹션 라벨 — 원본 9.5px · 자간 .12em 은 한글이 깨진다 */
  .pay-lbl { font-size: 11px !important; letter-spacing: .04em !important; }
  .pay-lbl i { width: 17px !important; height: 17px !important; font-size: 9.5px !important; }

  /* ══ 결제수단 칩 필터 ══ */
  .fopt { display: flex; flex-wrap: wrap; gap: 5px; }
  .fopt span { border: 1px solid #E4E8ED; background: #fff; border-radius: 3px;
    padding: 6px 11px; font-size: 11.5px; color: #6C7480; cursor: pointer; user-select: none; }
  .fopt span:hover { border-color: #C6CFD8; }
  .fopt span.on { border-color: #2F6490; background: #EEF4F9; color: #2F6490; font-weight: 600; }
  .fopt span.off { border-style: dashed; color: #C4CCD5; background: #FBFCFD; cursor: default; }

  /* ══ 결제창 상단 타이틀 ══ */
  .pay-topbar .ptl { position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%); display: flex; align-items: baseline; gap: 6px;
    white-space: nowrap; }
  .pay-topbar .ptl u { text-decoration: none; font-size: 15px; font-weight: 500;
    letter-spacing: .2em; color: #7A828E; }
  .pay-topbar .ptl b { font-size: 17px; font-weight: 700; letter-spacing: .1em;
    color: #171B22; }
  .tbf .pay-topbar .ptl u { font-size: 13.5px; }
  .tbf .pay-topbar .ptl b { font-size: 15.5px; }
  .mof .pay-topbar .ptl { gap: 5px; }
  .mof .pay-topbar .ptl u { font-size: 11px; letter-spacing: .14em; }
  .mof .pay-topbar .ptl b { font-size: 12.5px; letter-spacing: .06em; }

  /* 디스크립션 소제목 */
  .dcol .grp2 { font-family: "IBM Plex Mono", monospace; font-size: 10.5px; letter-spacing: .08em;
    color: #2F6490; margin: 16px 0 7px; padding-bottom: 5px; border-bottom: 1px solid #E4E8ED; }

  /* ══ 최근 결제 수단 ══ */
  .rrow { border: 1px solid #C6D8E6; background: #F5F9FC; border-radius: 5px; padding: 9px 11px; }
  .rrow .rl { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
  .rrow .rl em { font-style: normal; font-family: "IBM Plex Mono", monospace; font-size: 9.5px;
    letter-spacing: .09em; color: #2F6490; flex: none; }
  .rrow .rl s { text-decoration: none; font-size: 10.5px; color: #7E97AD; flex: none; }
  .rrow .rl i { flex: 1; height: 1px; background: #DCE8F1; }
  .rrow .cgd { grid-template-columns: repeat(6, 1fr); }

  /* ══ 채널 그리드 ══ */
  .cgrp { display: flex; align-items: center; gap: 9px; margin: 14px 0 8px; }
  .cgrp:first-child { margin-top: 0; }
  .cgrp em { font-style: normal; font-family: "IBM Plex Mono", monospace; font-size: 9.5px;
    letter-spacing: .09em; color: #6C7480; flex: none; }
  .cgrp s { text-decoration: none; font-size: 10.5px; color: #A0AAB5; flex: none; }
  .cgrp i { flex: 1; height: 1px; background: #EDF0F3; }

  .cgd { display: grid; grid-template-columns: repeat(6, 1fr); gap: 6px; }
  .ct { border: 1px solid #DDE3E9; border-radius: 4px; background: #fff; min-height: 60px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 4px; padding: 7px 4px; position: relative; cursor: pointer; }
  .ct:hover { border-color: #B9C3CE; }
  .ct .lg { display: flex; align-items: center; justify-content: center; min-height: 22px;
    font-size: 11.5px; font-weight: 700; color: #3D454F; letter-spacing: -.01em;
    text-align: center; line-height: 1.2; word-break: keep-all; }
  .ct .pgb { font-family: "IBM Plex Mono", monospace; font-size: 8.5px; font-weight: 500;
    letter-spacing: 0; padding: 1px 6px 2px; border-radius: 2px; }
  .ct .pgb.goc { background: #FFF4D6; color: #8A6A2F; border: 1px solid #EBDCB4; }
  .ct .pgb.one { background: #FBE9E9; color: #8C3A3A; border: 1px solid #EFD2D2; }
  .ct .pgb.etc { background: #EEF4F9; color: #2F6490; border: 1px solid #CFDEEA; }
  .ct.on { border-color: #2F6490; box-shadow: inset 0 0 0 1px #2F6490; background: #F7FAFC; }
  .ct.hosted { min-height: 66px; border-color: #C6CFD8; background: #FBFCFD; }
  .ct.hosted .lg { font-size: 13px; min-height: 28px; }
  .ct.hosted .hb { position: absolute; top: 3px; right: 4px;
    font-family: "IBM Plex Mono", monospace; font-size: 8px; color: #8A6A2F;
    background: #FFF9EC; border: 1px solid #EBDCB4; border-radius: 2px; padding: 0 4px 1px; }

  /* ══ 접힘 영역 · 스크롤 ══ */
  /* 스크롤 영역은 테두리로 경계를 만든다 — 펼치기 버튼은 이 박스 밖에 놓인다 */
  .cbox { position: relative; border: 1px solid #E4E8ED; border-radius: 5px;
    background: #FCFDFE; }
  .cwrap { box-sizing: border-box; padding: 10px; }
  .cwrap.fold { height: 290px; overflow-y: auto; }
  .cwrap.fold::-webkit-scrollbar { width: 8px; }
  .cwrap.fold::-webkit-scrollbar-track { background: transparent; }
  .cwrap.fold::-webkit-scrollbar-thumb { background: #CDD5DD; border-radius: 4px; }
  .cfade { display: none; position: absolute; left: 1px; right: 9px; bottom: 1px; height: 36px;
    pointer-events: none; border-radius: 0 0 5px 5px;
    background: linear-gradient(to bottom, rgba(252,253,254,0), #FCFDFE 82%); }
  .cbox.more .cfade { display: block; }
  .cmore { margin-top: 8px; border: 1px solid #D5DBE2; background: #fff; border-radius: 5px;
    height: 38px; display: flex; align-items: center; justify-content: center; gap: 7px;
    font-size: 12.5px; color: #3D454F; cursor: pointer; user-select: none; }
  .cmore:hover { border-color: #2F6490; color: #2F6490; }
  .cmore i { font-style: normal; font-size: 9px; color: #98A2AE; }
  .cmore.none { display: none; }

  /* ══ 게임 · 상품 정보 — 한 박스 · 구분선 · 상품 영역 배경 ══ */
  .ordbox { border: 1px solid #D5DBE2; border-radius: 6px; overflow: hidden; background: #fff; }
  .ord-game { display: flex; align-items: baseline; gap: 11px; padding: 10px 14px;
    border-bottom: 1px solid #E4E8ED; }
  .ord-game .k { font-family: "IBM Plex Mono", monospace; font-size: 10px;
    letter-spacing: .09em; color: #6C7480; flex: none; }
  .ord-game .v { font-size: 13.5px; font-weight: 600; color: #171B22; letter-spacing: -.015em; }

  .ord-item { display: flex; align-items: center; gap: 11px; padding: 14px;
    background: #F4F8FB; }
  .ord-item .thumb { width: 52px; height: 52px; flex: none; border: 1px solid #D3DEE7;
    border-radius: 5px; background: #fff; display: flex; align-items: center;
    justify-content: center; font-size: 9px; color: #A0AAB5; line-height: 1.35; text-align: center; }
  .ord-item .meta { display: flex; flex-direction: column; gap: 5px; min-width: 0; }
  .ord-item .ct2 { align-self: flex-start; border: 1px solid #DCE4EB; background: #fff;
    border-radius: 3px; padding: 3px 8px; font-size: 10px; color: #6C7480; }
  .ord-item .nm { font-size: 15px; font-weight: 600; color: #171B22; letter-spacing: -.02em; }

  .ord-item .prc { margin-left: auto; flex: none; font-family: "IBM Plex Mono", monospace;
    font-size: 15px; font-weight: 600; color: #171B22; letter-spacing: -.02em; }

  .qty { flex: none; display: flex; align-items: baseline; gap: 2px;
    font-family: "IBM Plex Mono", monospace; background: #fff; border: 1px solid #D3DEE7;
    border-radius: 4px; padding: 5px 11px 6px; }
  .qty s { text-decoration: none; font-size: 12px; color: #98A2AE; }
  .qty b { font-size: 18px; font-weight: 600; color: #171B22; letter-spacing: -.02em; }

  .tbf .ord-item .nm { font-size: 14px; }
  .mof .ord-game { padding: 9px 12px; gap: 9px; }
  .mof .ord-item { padding: 11px 12px; gap: 10px; }
  .mof .ord-item .thumb { width: 42px; height: 42px; }
  .mof .ord-item .nm { font-size: 13px; }
  .mof .qty b { font-size: 16px; }
  .mof .ord-item .prc { font-size: 13px; }
  .mof .ord-item { gap: 8px; }
  .tbf .ord-item .prc { font-size: 14px; }

  /* 버튼 하단 안내 */
  .btn-note { font-size: 11px; color: #98A2AE; line-height: 1.7; word-break: keep-all;
    margin-top: 11px; text-align: center; }

  /* TABLET · MO */
  .tbf .cgd, .tbf .rrow .cgd { grid-template-columns: repeat(4, 1fr); }
  .tbf .ct { min-height: 54px; }
  .tbf .ct .lg { font-size: 10.5px; }
  .tbf .cwrap.fold { height: 258px; }
  .mof .cgd, .mof .rrow .cgd { grid-template-columns: repeat(3, 1fr); gap: 5px; }
  .mof .ct { min-height: 54px; padding: 7px 3px; }
  .mof .ct .lg { font-size: 10.5px; min-height: 20px; }
  .mof .ct.hosted { min-height: 58px; }
  .mof .ct.hosted .lg { font-size: 12px; }
  .mof .cwrap.fold { height: 228px; }
</style>
"""

# ══════════════════ 채널 데이터 ══════════════════
# GGL 인도네시아 현행 운영 화면 실측 · GOCpay + OneOne
# 버튼 안에는 채널명과 결제사 배지만 둔다
HOSTED = ["Adyen", "Stripe", "Razer Gold", "Xsolla"]

GROUPS = [
    ("HOSTED",        "Hosted Checkout", "결제사 자체 결제창", [(n, None) for n in HOSTED]),
    ("CARD",          "CARD",            "신용 · 체크카드",     []),
    ("WALLET",        "WALLET",          "간편결제 · 지갑", [
        ("OVO", "goc"), ("GoPay", "goc"), ("ShopeePay", "goc"), ("DANA", "goc"),
        ("LinkAja", "goc"), ("QRIS", "goc"), ("ROKU Wallet", "goc"), ("Sakuku", "goc"),
        ("Jenius", "goc"), ("virgo", "goc"), ("GOC wallet", "goc"), ("OOC", "one"),
    ]),
    ("BANK",          "BANK",            "계좌 · 가상계좌", [
        ("mandiri", "goc"), ("BRI", "goc"), ("BCA", "goc"), ("BNI", "goc"),
        ("PermataBank", "goc"), ("CIMB NIAGA", "goc"), ("CIMB Clicks", "goc"),
        ("BANK TRANSFER", "one"),
    ]),
    ("OTC",           "OTC / VOUCHER",   "편의점 · 오프라인 수납", [
        ("Alfamart", "goc"), ("Indomaret", "goc"),
    ]),
    ("CARRIER",       "CARRIER",         "통신사 결제",        []),
    ("PREPAID",       "PREPAID / PIN",   "선불 · 핀 코드", [
        ("Game-on", "goc"),
    ]),
]
RECENT = [("OVO", "goc"), ("mandiri", "goc"), ("Alfamart", "goc")]

NCH = sum(len(g[3]) for g in GROUPS)
PGN = {"goc": "GOCpay", "one": "OneOne", "razer": "Razer"}
PGC = {"goc": "goc", "one": "one", "razer": "etc"}


def tile(name, pg, on=False, hosted=False):
    lg = '<span class="lg">%s</span>' % name
    if hosted:
        return ('<div class="ct hosted%s"><span class="hb">HOSTED</span>%s</div>'
                % (" on" if on else "", lg))
    return ('<div class="ct%s">%s<span class="pgb %s">%s</span></div>'
            % (" on" if on else "", lg, PGC[pg], PGN[pg]))


def chips():
    o = []
    o.append('<span class="on" data-f="ALL">ALL</span>')
    for code, label, ko, items in GROUPS:
        if items:
            o.append('<span data-f="%s">%s</span>' % (code, label))
        else:
            o.append('<span class="off">%s</span>' % label)
    return '<div class="fopt" data-role="chips">%s</div>' % "".join(o)


def recent():
    t = "".join("  " + tile(n, pg) for n, pg in RECENT)
    return ('<div class="rrow"><span class="rl"><em>RECENT</em>'
            '<s>최근 결제 수단 · %d</s><i></i></span>'
            '<div class="cgd">%s</div></div>' % (len(RECENT), t))


def channels():
    o = []
    for code, label, ko, items in GROUPS:
        if not items:
            continue
        o.append('<div class="cgrp" data-g="%s"><em>%s</em><s>%s · %d</s><i></i></div>'
                 % (code, label.upper(), ko, len(items)))
        o.append('<div class="cgd" data-g="%s">' % code)
        for n, pg in items:
            o.append("  " + tile(n, pg, hosted=(code == "HOSTED")))
        o.append('</div>')
    return "\n              ".join(o)


CARD = '''
          <div class="pay-card">

            <!-- 1 · 게임 · 상품 -->
            <div class="pay-sec">
              <span class="pay-lbl"><i>1</i> 게임 · 상품 정보</span>
              <div class="ordbox">
                <div class="ord-game">
                  <span class="k">게임</span>
                  <span class="v">라그나로크 어비스</span>
                </div>
                <div class="ord-item">
                  <span class="thumb">상품<br>이미지</span>
                  <span class="meta">
                    <span class="ct2">소비</span>
                    <span class="nm">프리미엄 성장석</span>
                  </span>
                  <span class="prc">USD 2.50</span>
                  <span class="qty"><s>&times;</s><b>2</b></span>
                </div>
              </div>
            </div>

            <!-- 2 · 결제수단 선택 -->
            <div class="pay-sec">
              <span class="pay-lbl"><i>2</i> 결제수단 선택 <b>필수</b></span>
              %s
              %s
              <div class="cbox">
                <div class="cwrap fold" data-role="cwrap">
              %s
                </div>
                <span class="cfade"></span>
              </div>
              <div class="cmore" data-role="more"><span>펼쳐 보기</span><i>&#9662;</i></div>
            </div>

            <!-- 3 · 결제 동의 -->
            <div class="pay-sec">
              <span class="pay-lbl"><i>3</i> 결제 동의 <b>필수</b></span>
              <div class="agree must"><span class="cb"></span><span class="tt"><b>[필수]</b> 인게임 재화는 <b>우편 수령 후 청약철회가 제한</b>됩니다. 결제 정보 · 지급 대상을 확인했습니다.</span><span class="lk">전문</span></div>
              <div class="agree must"><span class="cb"></span><span class="tt"><b>[필수]</b> 만 19세 미만은 법정대리인의 동의가 필요하며, 동의 없는 결제는 취소될 수 있습니다.</span></div>
            </div>

            <!-- 4 · 결제 -->
            <div class="pay-sec">
              <span class="pay-lbl"><i>4</i> 결제</span>
              <div class="paybtn"><span class="a">USD 5.00</span><span class="b">결제하기</span></div>
              <p class="btn-note">최종 결제 금액이며 선택한 결제수단에 따라 카드사 해외이용 수수료가 별도로 붙을 수 있습니다.</p>
            </div>

          </div>''' % (chips(), recent(), channels())

PC = '''
      <div class="pane pane-pc on">
      <div class="wstage">
      <div class="pcframe pay-page" style="width:1440px;display:flex;flex-direction:column;position:relative;">

        <div class="sec pay-topbar" style="position:relative;">
          <div class="mk" style="position:absolute;top:18px;left:-10px;">5</div>
          <div class="mk" style="position:absolute;top:38px;left:-10px;">6</div>
          <span class="bk"></span>
          <span class="ptl"><u>RAGNAROK</u><b>ONE PAY</b></span>
        </div>

        <div class="pay-col" style="position:relative;">
          <div class="mk" style="position:absolute;top:42px;left:-34px;">1</div>
          <div class="mk" style="position:absolute;top:229px;left:-34px;">2</div>
          <div class="mk" style="position:absolute;top:640px;left:-34px;">3</div>
          <div class="mk" style="position:absolute;top:779px;left:-34px;">4</div>
%s
        </div>
      </div>
      </div>
      </div>
''' % CARD

TB = '''
      <div class="pane pane-tb">
      <div class="wstage">
      <div class="pcframe" style="display:flex;flex-direction:column;position:relative;">
        <div class="tbf" style="width:768px;background:#F7F8FA;border-radius:4px;overflow:hidden;">
          <div class="sec pay-topbar" style="position:relative;"><span class="bk"></span><span class="ptl"><u>RAGNAROK</u><b>ONE PAY</b></span></div>
          <div class="pay-col" style="max-width:680px;padding:18px 22px 26px;">
%s
          </div>
        </div>
      </div>
      </div>
      </div>
''' % CARD

MO = '''
      <div class="pane pane-mo">
      <div class="wstage">
      <div class="pcframe" style="display:flex;flex-direction:column;position:relative;">
        <div class="mof" style="width:390px;background:#F7F8FA;border-radius:14px;overflow:hidden;">
          <div class="sec pay-topbar" style="height:48px;padding:0 16px;position:relative;"><span class="bk"></span><span class="ptl"><u>RAGNAROK</u><b>ONE PAY</b></span></div>
          <div class="pay-col" style="max-width:100%%;padding:14px 14px 22px;">
%s
          </div>
        </div>
      </div>
      </div>
      </div>
''' % CARD

DESC = '''
    <div class="dcol">
      <h4>ONE-PAY · 라그나로크원페이 화면정의서</h4>

      <div class="imm">
        <div class="imm-h">이 화면의 기준</div>
        <div class="imm-r"><span class="imm-k">선택 단위</span><span class="imm-v"><b>depth 2 채널</b> — 대분류를 클릭해 들어가는 뎁스를 두지 않는다</span></div>
        <div class="imm-r"><span class="imm-k">대분류</span><span class="imm-v"><b>칩 필터</b>로만 쓴다 — 목록을 좁히는 도구이고 화면 계층이 아니다</span></div>
        <div class="imm-r"><span class="imm-k">통화</span><span class="imm-v"><b>선택 UI 없음</b> — 웹샵에서 확정된 통화로 진입한다</span></div>
        <div class="imm-r"><span class="imm-k">수량</span><span class="imm-v"><b>표시만</b> — 변경 · 삭제 불가</span></div>
        <div class="imm-r"><span class="imm-k">금액</span><span class="imm-v"><b>결제 버튼에만</b> 표기 — 상단 금액 영역을 두지 않는다</span></div>
        <div class="imm-r"><span class="imm-k">샘플 데이터</span><span class="imm-v">GGL 인도네시아 <b>현행 운영 화면 실측</b> · <span class="mono">GOCpay · OneOne</span> · 채널 %d개</span></div>
        <div class="imm-r"><span class="imm-k">카드 부재</span><span class="imm-v">로컬 결제사가 카드를 취급하지 않아 <b>CARD 분류가 비어 있다</b> — 카드는 Hosted Checkout으로 처리한다</span></div>
      </div>

      <div class="dr">
        <div class="dr-h"><span class="mk">1</span><span class="dr-t">게임 · 상품 정보</span><span class="src">행 1</span></div>
        <p class="dr-b">게임명과 구매 상품만 표시한다. <b>서버 · 캐릭터명은 이 화면에 두지 않는다</b> — 지급 대상은 웹샵에서 이미 확정됐고, 결제창에서 반복 표기할 이유가 없다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">게임</span><span class="spec-v">게임명 1행. 어느 게임의 결제인지만 확인시킨다</span></div>
          <div class="spec-r"><span class="spec-k">서버 · 계정 한정 상품</span><span class="spec-v"><b>예외적으로 표시한다.</b> 서버 한정 또는 계정 한정 상품은 <b>웹샵 화면에서 서버명 · 계정명을 선택</b>해야 하며, 통합결제창에서도 <b>해당 항목을 함께 표기</b>한다 — 잘못된 서버 · 계정으로 지급되면 회수가 불가능하다</span></div>
          <div class="spec-r"><span class="spec-k">표기 위치</span><span class="spec-v">게임 행 <b>오른쪽 끝</b>에 <span class="mono">서버 발할라</span> 또는 <span class="mono">계정 gv_****</span>를 덧붙인다. 한정 상품이 아니면 이 칸이 없다</span></div>
          <div class="spec-r"><span class="spec-k">박스 구성</span><span class="spec-v"><b>게임과 상품을 한 박스에 묶고 구분선으로 나눈다.</b> 위는 흰 배경의 게임 행, 아래는 <b>연한 배경의 상품 영역</b>이다 — 구매 대상이 먼저 눈에 들어와야 한다</span></div>
          <div class="spec-r"><span class="spec-k">상품 영역</span><span class="spec-v">썸네일 <b>52</b> · 분류 태그 · 상품명 · <b>단가</b> · 수량. 배경을 깔아 게임 행과 층을 분리한다</span></div>
          <div class="spec-r"><span class="spec-k">금액 표기</span><span class="spec-v">상품 우측에 <b>단가</b>를 둔다 — <span class="mono">USD 2.50</span> 뒤에 <span class="mono">&times; 2</span>가 이어져 <b>단가라는 것이 위치로 드러난다.</b> 별도 라벨을 붙이지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">합계와의 관계</span><span class="spec-v">합계는 <b>결제 버튼에만</b> 표기한다 — 상품 영역은 <b>단가 &times; 수량</b>, 버튼은 <b>최종 결제 금액</b>이다. 같은 금액을 두 번 쓰지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">통화</span><span class="spec-v">단가와 버튼 금액은 <b>같은 통화</b>다. 웹샵에서 확정된 통화를 그대로 쓰며 결제창에서 환산하지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">상품</span><span class="spec-v">이미지 · 분류 태그 · 상품명 · <b>수량</b>. 상품가 · 세액을 분해하지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">수량</span><span class="spec-v"><span class="mono">&times; 2</span>를 <b>흰 배경 칩</b>으로 우측에 둔다 — 연한 배경 위에서 값이 도드라진다. <b>수량 변경 · 삭제 컨트롤을 두지 않는다</b> — 주문은 웹샵에서 확정되며 결제창에서 금액이 달라질 수 없다</span></div>
        </div>
      </div>

      <div class="dr-alt">
        <div class="dr-h"><span class="mk">2</span><span class="dr-t">결제수단 선택</span><span class="src">행 2 · 핵심</span></div>
        <p class="dr-b">한 섹션 안에 <b>칩 필터 → 최근 결제 수단 → 채널 그리드</b> 순으로 놓는다. 분류는 구분선으로만 나뉘고 클릭 대상이 아니다.</p>

        <div class="grp2">칩 필터</div>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">위치</span><span class="spec-v"><b>섹션 제목 바로 아래.</b> 별도 섹션으로 분리하지 않는다 — 결제수단을 고르는 행위의 일부다</span></div>
          <div class="spec-r"><span class="spec-k">기본값</span><span class="spec-v"><b>ALL</b> — 진입 시 전체 채널이 보인다. 필터는 찾기 어려울 때만 쓴다</span></div>
          <div class="spec-r"><span class="spec-k">전체 정의</span><span class="spec-v"><span class="mono">ALL · Hosted Checkout · CARD · WALLET · BANK · OTC/VOUCHER · CARRIER · PREPAID/PIN</span> — <b>8개 고정</b></span></div>
          <div class="spec-r"><span class="spec-k">동작</span><span class="spec-v">칩을 누르면 <b>해당 분류만 남기고 나머지를 숨긴다.</b> 최근 결제 수단 행도 그 분류에 속한 것만 남는다</span></div>
          <div class="spec-r"><span class="spec-k">자동 제외</span><span class="spec-v">해당 법인에 <b>채널이 0개인 분류는 누를 수 없다</b>. 화면 예시의 <b>점선 회색</b>이 그 상태다 — 실제 화면에서는 칩 자체가 빠진다</span></div>
          <div class="spec-r"><span class="spec-k">샘플의 제외 분류</span><span class="spec-v"><span class="mono">CARD · CARRIER</span> 2개. 인도네시아 결제사가 카드 취득과 통신사 결제를 취급하지 않는다</span></div>
        </div>

        <div class="grp2">최근 결제 수단</div>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">위치</span><span class="spec-v">채널 그리드 <b>첫 행</b>. 파란 배경으로 구분해 일반 목록과 섞이지 않게 한다</span></div>
          <div class="spec-r"><span class="spec-k">헤더 표기</span><span class="spec-v"><span class="mono">RECENT</span> + 「최근 결제 수단 · N」 — <b>아래 분류 헤더와 같은 형식</b>이다. 영문 코드를 앞에 두고 한글 설명과 개수를 뒤에 붙인다</span></div>
          <div class="spec-r"><span class="spec-k">개수</span><span class="spec-v"><b>최대 3개.</b> 그 이상 두면 최근이라는 의미가 흐려지고 아래 목록과 중복이 커진다</span></div>
          <div class="spec-r"><span class="spec-k">기준</span><span class="spec-v">해당 계정의 <b>최근 결제 성공 건</b>에서 중복을 제거해 최신순 3개. 비회원은 이 행이 없다</span></div>
          <div class="spec-r"><span class="spec-k">중복 노출</span><span class="spec-v">아래 목록에도 <b>같은 채널이 그대로 남는다.</b> 최근 행은 지름길이고, 목록은 전체를 훑는 용도다</span></div>
          <div class="spec-r"><span class="spec-k">필터 무관</span><span class="spec-v"><b>칩 선택의 영향을 받지 않는다.</b> 어떤 분류를 걸어도 이 행은 그대로 남는다 — 최근 쓴 수단으로 가는 지름길이므로 필터 대상이 아니다</span></div>
        </div>

        <div class="grp2">채널 그리드</div>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">Hosted Checkout</span><span class="spec-v"><b>결제사 로고 버튼만</b> 둔다. 내부 결제수단은 그 결제사 화면에서 고르므로 <b>우리가 노출하지 않는다</b> — <span class="mono">Adyen · Stripe · Razer Gold · Xsolla</span></span></div>
          <div class="spec-r"><span class="spec-k">Hosted 판별 기준</span><span class="spec-v"><b>자기 결제창을 띄우고 그 안에서 결제수단을 선택하게 하는 것</b>만 여기 둔다. 자체 지갑이라도 우리 화면에서 바로 결제되면 <b>WALLET에 들어간다</b> — <span class="mono">GOC wallet · OOC</span>가 그 예다</span></div>
          <div class="spec-r"><span class="spec-k">개별 채널</span><span class="spec-v"><b>채널 로고 + 결제사 배지를 한 버튼 안에</b> 표시한다. 같은 채널을 여러 결제사가 지원해도 <b>1순위 결제사 배지만</b> 붙인다</span></div>
          <div class="spec-r"><span class="spec-k">버튼 내 문구</span><span class="spec-v"><b>채널 로고와 결제사 배지 둘만 둔다.</b> 「가상계좌」 「국가 표준 QR」 「편의점」 같은 부제를 넣지 않는다 — 로고가 이미 그 정보를 담고 있고, 타일이 좁아 읽히지도 않는다</span></div>
          <div class="spec-r"><span class="spec-k">중복 통합</span><span class="spec-v"><span class="mono">OVO · DANA · LinkAja</span>는 <span class="mono">GOCpay</span>와 <span class="mono">OneOne</span>이 모두 지원한다. <b>1타일로 합치고 1순위 결제사로 전송</b>한다 — 같은 채널이 두 번 나오면 유저가 고를 수 없다</span></div>
          <div class="spec-r"><span class="spec-k">1순위 결정</span><span class="spec-v">어드민에서 <b>채널별 1순위 · 2순위 결제사</b>를 지사가 지정한다. 서버는 판단하지 않고 그 값을 읽는다. 1순위 장애 시에만 2순위로 넘긴다</span></div>
          <div class="spec-r"><span class="spec-k">열 수</span><span class="spec-v">PC <b>6열</b> / TABLET <b>4열</b> / MO <b>3열</b>. 로고 이미지를 쓰므로 좁은 폭에도 담긴다</span></div>
          <div class="spec-r"><span class="spec-k">로고</span><span class="spec-v"><b>어드민 등록 이미지</b>를 쓴다. 텍스트 라벨로는 6열이 성립하지 않는다 — 화면 예시는 로고 자리에 이름을 넣은 상태다</span></div>
          <div class="spec-r"><span class="spec-k">카드가 있는 법인</span><span class="spec-v"><span class="mono">VISA · MC · JCB</span>를 <b>1타일에 로고 병기</b>한다. 카드사를 고르지 않는다 — 브랜드는 카드번호로 <b>자동 판별</b>된다</span></div>
          <div class="spec-r"><span class="spec-k">카드가 없는 법인</span><span class="spec-v"><b>이 샘플은 CARD 분류가 비어 있다.</b> 인도네시아 결제사 <span class="mono">GOCpay · OneOne</span>은 <b>은행 · 통신사 · 편의점 · 전자화폐</b>를 취급하고 <b>카드 취득은 하지 않는다</b>. 카드 결제는 <b>Hosted Checkout의 <span class="mono">Adyen · Stripe</span> 결제창</b>으로 처리한다 — <b>카드를 기본 분류로 전제하면 안 된다</b></span></div>
          <div class="spec-r"><span class="spec-k">정렬</span><span class="spec-v">Hosted Checkout &rarr; CARD &rarr; WALLET &rarr; BANK &rarr; OTC/VOUCHER &rarr; CARRIER &rarr; PREPAID/PIN. <b>지역 점유율 순으로 어드민에서 조정</b>한다</span></div>
        </div>

        <div class="grp2">영역 접힘 · 펼쳐 보기</div>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">문제</span><span class="spec-v">채널이 <b>20개를 넘으면</b> 결제 버튼이 화면 밖으로 밀린다. 인도네시아는 27개다</span></div>
          <div class="spec-r"><span class="spec-k">접힘 높이</span><span class="spec-v">PC <b>290</b> / TABLET <b>258</b> / MO <b>228</b>. 이 안에서 <b>스크롤로 전체를 볼 수 있다</b> — 접힘이 곧 차단은 아니다</span></div>
          <div class="spec-r"><span class="spec-k">영역 경계</span><span class="spec-v">스크롤 영역을 <b>테두리 박스로 감싼다.</b> <b>펼쳐 보기 버튼은 이 박스 밖</b>에 둔다 — 스크롤 안에 있으면 목록을 내리는 동안 버튼이 따라 움직여 누를 수 없다</span></div>
          <div class="spec-r"><span class="spec-k">크기 고정</span><span class="spec-v"><b>내용 길이와 무관하게 높이를 고정</b>한다. 칩으로 걸러 채널이 1개만 남아도 영역이 줄어들지 않는다 — <b>필터를 바꿀 때마다 아래 동의 · 결제 버튼 위치가 흔들리면 안 된다</b></span></div>
          <div class="spec-r"><span class="spec-k">하단 페이드</span><span class="spec-v"><b>숨은 채널이 있을 때만</b> 흰색 그라데이션을 덮어 아래가 더 있음을 알린다. 목록이 끝났다고 오인하지 않도록 — 다 보이는 상태에서는 페이드를 걷는다</span></div>
          <div class="spec-r"><span class="spec-k">펼쳐 보기</span><span class="spec-v">라벨은 <span class="mono">펼쳐 보기</span> 하나다. <b>숨은 개수를 표기하지 않는다</b> — 스크롤로 이미 전체를 볼 수 있어 개수가 판단에 쓰이지 않는다. 클릭하면 높이 제한이 풀리고 <b>접기</b>로 바뀐다</span></div>
          <div class="spec-r"><span class="spec-k">버튼 노출 조건</span><span class="spec-v">내용이 <b>접힘 높이를 넘을 때만</b> 버튼을 둔다. 필터를 걸어 남는 것이 다 들어가면 <b>버튼 자체를 숨긴다</b></span></div>
          <div class="spec-r"><span class="spec-k">기기별 적용</span><span class="spec-v"><b>PC · TABLET · MO 모두 동일하게 동작</b>한다. 접힘 높이만 다르고 버튼과 페이드 규칙은 같다</span></div>
          <div class="spec-r"><span class="spec-k">스크롤 무반응</span><span class="spec-v">목록을 스크롤해도 <b>버튼 라벨과 상태가 변하지 않는다</b> — 스크롤 중에 버튼이 바뀌면 조작이 흔들린다. 필터 변경과 창 크기 변경에만 다시 판정한다</span></div>
          <div class="spec-r"><span class="spec-k">선택 유지</span><span class="spec-v">접었을 때 <b>선택한 채널이 접힘 영역 밖에 있으면</b> 그 위치로 스크롤을 맞춘다 — 선택이 보이지 않는 상태를 만들지 않는다</span></div>
        </div>

        <div class="grp2">선택 이후</div>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">Hosted Checkout</span><span class="spec-v">결제 버튼을 누르면 <b>해당 결제사 결제창으로 전환</b>된다. 우리 화면에서 추가 입력을 받지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">개별 채널</span><span class="spec-v">앱 또는 결제사 페이지로 전환된 뒤 돌아온다. <b>중간 선택 화면이 없다</b></span></div>
          <div class="spec-r"><span class="spec-k">구독 상품</span><span class="spec-v">정기결제 불가 채널은 <b>목록에서 제외</b>한다. 인도네시아는 대부분이 불가이므로 구독 판매 시 노출 채널이 급감한다</span></div>
        </div>
      </div>

      <div class="dr">
        <div class="dr-h"><span class="mk">3</span><span class="dr-t">결제 동의</span><span class="src">행 3</span></div>
        <p class="dr-b">동의 문구는 <b>상품 유형별 어드민 입력</b>으로 관리한다. 통화 선택을 두지 않으므로 통화 확인 문장은 빠진다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">CTA 조건</span><span class="spec-v">필수 항목을 <b>전부 체크</b>해야 핀 4의 결제 버튼이 활성화된다. <b>결제수단 선택과 함께 두 조건이 모두 충족</b>되어야 한다</span></div>
          <div class="spec-r"><span class="spec-k">환불 고지</span><span class="spec-v">「결제 완료 후 <b>자동 환불이 제공되지 않으며</b>, 환불 문의는 <b>고객센터</b>로 접수해야 합니다」를 필수 고지로 노출한다</span></div>
          <div class="spec-r"><span class="spec-k">취소 불가 채널</span><span class="spec-v">편의점 수납 · 선불 핀처럼 <b>온라인 취소가 불가한 채널</b>을 선택한 경우 별도 확인 팝업을 띄운다</span></div>
        </div>
      </div>

      <div class="dr-alt">
        <div class="dr-h"><span class="mk">4</span><span class="dr-t">결제 버튼 · 금액</span><span class="src">행 4 · 하단</span></div>
        <p class="dr-b"><b>금액은 결제 버튼에만 표기</b>한다. 상단 금액 영역을 없애 화면에서 금액이 한 번만 나온다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">라벨</span><span class="spec-v">웹샵에서 확정된 통화와 금액을 그대로 반영 — <span class="mono">USD 5.00 결제하기</span>. <b>통화 코드를 함께 표기</b>한다 — 다국가 서비스에서 기호만으로는 구분되지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">안내 문구</span><span class="spec-v"><b>버튼 하단</b>에 둔다. 수수료 · 세금 관련 고지가 금액 바로 아래에서 읽히도록 배치</span></div>
          <div class="spec-r"><span class="spec-k">고정</span><span class="spec-v">MO는 처음부터 하단 고정. PC는 뷰포트를 벗어나면 승격</span></div>
        </div>

        <div class="grp2">버튼 활성 조건</div>
        <p class="dr-b"><b>필수 항목을 모두 충족했을 때만 버튼이 활성화된다.</b> 진입 시점에는 비활성 상태로 시작한다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">조건 1 · 결제수단</span><span class="spec-v"><b>1개를 선택</b>해야 한다. 최근 결제 수단 행에서 골라도 같다. 진입 시 <b>기본 선택을 두지 않는다</b> — 유저가 고르지 않은 수단으로 결제되면 안 된다</span></div>
          <div class="spec-r"><span class="spec-k">조건 2 · 필수 동의</span><span class="spec-v">핀 3의 <b>필수 항목을 전부 체크</b>해야 한다. 선택 항목은 활성 여부에 영향을 주지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">판정 시점</span><span class="spec-v">두 조건을 <b>즉시 재판정</b>한다. 체크를 해제하거나 결제수단 선택이 풀리면 <b>바로 비활성으로 돌아간다</b></span></div>
          <div class="spec-r"><span class="spec-k">비활성 표기</span><span class="spec-v"><span class="mono">.paybtn.dis</span> — 배경을 옅게 낮춘다. <b>사유 문구를 버튼에 붙이지 않는다</b> — 체크 · 선택 미완료 상태는 화면에서 이미 드러난다</span></div>
          <div class="spec-r"><span class="spec-k">비활성 클릭</span><span class="spec-v">클릭을 무시하지 않고 <b>미충족 항목으로 스크롤</b>한 뒤 해당 영역을 <b>한 번 강조</b>한다 — 왜 눌리지 않는지 유저가 스스로 찾게 두지 않는다</span></div>
          <div class="spec-r"><span class="spec-k">한정 상품</span><span class="spec-v">서버 · 계정 한정 상품은 <b>웹샵에서 대상이 확정된 뒤에만</b> 이 화면에 들어온다. 결제창에서 대상을 고르는 절차가 없으므로 <b>활성 조건에 추가되지 않는다</b></span></div>
          <div class="spec-r"><span class="spec-k">중복 클릭 차단</span><span class="spec-v">누른 직후 <b>버튼을 비활성으로 전환</b>하고 결제 세션 응답까지 유지한다 — 연타로 세션이 두 번 생기면 중복 결제가 된다</span></div>
        </div>
      </div>

      <div class="dr">
        <div class="dr-h"><span class="mk">5</span><span class="dr-t">상단 바 · 페이지 방식 · 진입 경로</span><span class="src">전역</span></div>
        <p class="dr-b"><b>모달 · 팝업 · iframe이 아닌 독립 URL 페이지</b>다. PG 3DS · 리다이렉트 인증이 팝업 · iframe 안에서 정상 동작하지 않는다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">상단 바</span><span class="spec-v">중앙에 <b>RAGNAROK ONE PAY</b>를 표시한다. 좌측 뒤로가기 옆에는 <b>텍스트를 두지 않는다</b> — 타이틀이 중앙에 있어 중복이다</span></div>
          <div class="spec-r"><span class="spec-k">표기 대상</span><span class="spec-v">게임 정보는 핀 1로 분리했으므로 상단 바에서 중복 표기하지 않는다. <b>지사명 · 법인 코드는 노출하지 않는다</b></span></div>
          <div class="spec-r"><span class="spec-k">보안 배지</span><span class="spec-v"><span class="mono">SSL · PCI-DSS</span> 배지는 노출하지 않는다. 카드 정보 비보관 · 키 격리는 서버 요건이며 화면 표기 대상이 아니다</span></div>
          <div class="spec-r"><span class="spec-k">전달값</span><span class="spec-v">호출측(웹샵 · 인게임 · 지사 포털)은 <b>머천트 · 게임 id · 상품 코드 · 수량 · 지급 대상</b>만 전달한다. <b>금액 · 통화 · 결제수단은 전달하지 않는다</b> — 금액은 서버가 산출한다</span></div>
        </div>
        <div class="imm">
          <div class="imm-h">통합결제창 이용 범위</div>
          <div class="imm-r"><span class="imm-k">웹샵</span><span class="imm-v"><b><a href="webshop-ui.html" style="color:#2F6490;">웹샵 화면정의서</a></b>의 [결제하기]</span></div>
          <div class="imm-r"><span class="imm-k">인게임</span><span class="imm-v">게임 안 상점의 구매하기</span></div>
          <div class="imm-r"><span class="imm-k">지사 포털</span><span class="imm-v">포털 내 상품 구매 — 포인트 충전 등</span></div>
        </div>
      </div>

      <div class="dr-alt">
        <div class="dr-h"><span class="mk">6</span><span class="dr-t">결제 모듈 — 조직 · 자금 구조</span><span class="src">전역</span></div>
        <p class="dr-b">이 화면을 읽는 데 필요한 범위에서 <b>조직 · 자금 구조</b>를 정리한다. 상세는 각 설계 문서에 있다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">전제</span><span class="spec-v">지사별로 개별 구축했던 결제를 <b>본사가 단일 구성으로 제공하고 지사가 연동해 사용</b>한다 — 결제창 1종 · PG 연동은 PG사당 1회</span></div>
          <div class="spec-r"><span class="spec-k">자금 경로</span><span class="spec-v">결제 대금은 <b>본사를 경유하지 않고 PG사에서 각 지사 법인 계좌로 직접 입금</b>된다. 매출도 해당 법인에 귀속된다 — 구조는 <b><a href="../wiki/planning/payment-webshop-structure.html#b1" style="color:#2F6490;">웹샵/통합결제 구조</a></b> 참조</span></div>
          <div class="spec-r"><span class="spec-k">역할 분담</span><span class="spec-v">본사는 <b>결제창 · 웹샵 제공 · PG 어댑터 · 키 격리 보관</b>, 지사는 <b>PG 계약 · 결제수단 · 가격 · 환불 · 정산</b>을 담당한다</span></div>
          <div class="spec-r"><span class="spec-k">결제 흐름</span><span class="spec-v">상품 선택(웹샵 · 인게임) &rarr; 지급 대상 확정 &rarr; <b>결제수단 선택 및 결제(이 화면)</b> &rarr; 지급 웹훅 &rarr; <b>게임 내 계정 우편함 수령</b></span></div>
        </div>
        <div class="imm">
          <div class="imm-h">확정 필요</div>
          <div class="imm-r"><span class="imm-k">로고 확보</span><span class="imm-v">채널 로고를 <b>지사가 등록</b>하는지 본사가 공용 세트를 제공하는지</span></div>
          <div class="imm-r"><span class="imm-k">Hosted 범위</span><span class="imm-v">MyCard · GASH도 자체 결제창을 띄우는지 — 띄우면 <b>대만 채널이 6개로 줄어든다</b></span></div>
          <div class="imm-r"><span class="imm-k">1순위 기준</span><span class="imm-v">중복 채널의 1순위 결제사를 <b>수수료 · 정산 주기 · 승인율</b> 중 무엇으로 정할지</span></div>
        </div>
      </div>

    </div>
''' % NCH

APP = '''
<div class="app">
  <nav class="nav">
    <span class="brand"><b>RAGNAROK PORTAL</b><span>라그나로크원페이 화면정의서</span></span>
    <span class="nvg">라그나로크원페이</span>
    <button type="button" class="nv" data-go="s09"><b>ONE-PAY</b><span>라그나로크원페이</span></button>
    <span class="ctl">
      <a href="payment-checkout-currency.html" class="desc-btn" style="text-decoration:none;">
        <i>&#9656;</i><span>구안 · 통화 선택형</span>
      </a>
      <button type="button" class="desc-btn" id="descBtn" title="D">
        <i>&#9776;</i><span class="lbl-on">디스크립션 접기</span><span class="lbl-off">디스크립션 펴기</span>
      </button>
    </span>
  </nav>
  <div class="stage">
<section class="screen" id="s09">
<div style="width:100%;height:100%;background:#E9EBEF;display:flex;flex-direction:column;overflow:hidden;">
  <div class="shd"><span class="id">ONE-PAY</span><span class="nm">라그나로크원페이</span></div>
  <div class="wrap2">
    <div class="wcol is-pc">
      <div class="tabs">
        <button type="button" class="tab tab-on" data-dev="pc">PC</button>
        <button type="button" class="tab" data-dev="tb">TABLET</button>
        <button type="button" class="tab" data-dev="mo">MO</button>
      </div>
''' + PC + TB + MO + '''    </div>
''' + DESC + '''  </div>
</div>
</section>
  </div>
</div>
'''

# ══════════════════ 동작 스크립트 ══════════════════
JS2 = """
<script>
/* 결제수단 — 칩 필터 · 채널 선택 · 접힘 및 펼쳐 보기 */
(function () {
  function each(l, f) { Array.prototype.slice.call(l).forEach(f); }

  var syncs = [];   // 판정 함수 — 비활성 탭은 높이가 0이라 탭 전환 후 다시 재야 한다

  each(document.querySelectorAll('.pay-sec'), function (sec) {
    var chips = sec.querySelector('[data-role="chips"]');
    var wrap  = sec.querySelector('[data-role="cwrap"]');
    var more  = sec.querySelector('[data-role="more"]');
    if (!chips || !wrap || !more) return;

    var cbox  = sec.querySelector('.cbox');
    var cur = 'ALL';

    function applyFilter() {
      // 최근 결제 수단 행은 칩 선택의 영향을 받지 않는다 — 항상 그대로 노출한다
      each(wrap.querySelectorAll('.cgrp, .cgd'), function (el) {
        var g = el.getAttribute('data-g');
        el.style.display = (cur === 'ALL' || g === cur) ? '' : 'none';
      });
      sync();
    }

    function sync() {
      if (!wrap.classList.contains('fold')) {
        more.innerHTML = '<span>접기</span><i>&#9652;</i>';
        more.classList.remove('none');
        if (cbox) cbox.classList.remove('more');
        return;
      }
      // 넘치는지만 본다 — 스크롤 위치에 따라 바뀌지 않는다
      var over = wrap.scrollHeight > wrap.clientHeight + 2;
      more.innerHTML = '<span>펼쳐 보기</span><i>&#9662;</i>';
      if (over) { more.classList.remove('none'); }
      else { more.classList.add('none'); }
      if (cbox) { over ? cbox.classList.add('more') : cbox.classList.remove('more'); }
    }

    chips.addEventListener('click', function (e) {
      var c = e.target.closest('span');
      if (!c || c.classList.contains('off') || !c.dataset.f) return;
      each(chips.querySelectorAll('span'), function (x) { x.classList.remove('on'); });
      c.classList.add('on');
      cur = c.dataset.f;
      wrap.scrollTop = 0;
      applyFilter();
    });

    more.addEventListener('click', function () {
      wrap.classList.toggle('fold');
      sync();
    });

    sec.addEventListener('click', function (e) {
      var t = e.target.closest('.ct');
      if (!t) return;
      each(sec.querySelectorAll('.ct'), function (x) { x.classList.remove('on'); });
      t.classList.add('on');
    });

    syncs.push(sync);
    applyFilter();
    setTimeout(sync, 80);
  });

  function resync() { syncs.forEach(function (f) { f(); }); }

  // PC · TABLET · MO 탭을 바꾸면 보이게 된 프레임을 다시 판정한다
  document.addEventListener('click', function (e) {
    if (e.target.closest('.tab')) setTimeout(resync, 70);
  });
  window.addEventListener('resize', resync);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(resync);
})();
</script>
"""


def docnav(cur):
    css = io.open("_build/_docnav_css.html", encoding="utf-8").read()
    L = ['<div id="docnav">', '  <div id="docnav-m">']
    for g, items in NAV:
        L.append('    <div class="g">%s</div>' % g)
        for path, label in items:
            on = ' class="on"' if path == cur else ''
            L.append('    <a href="%s"%s>%s</a>' % (rel(cur, path), on, label))
    L += ['  </div>', '  <span id="docnav-b">문서 <i>&#9650;</i></span>', '</div>',
          '<script>', '(function () {',
          "  var n = document.getElementById('docnav'), b = document.getElementById('docnav-b');",
          "  b.addEventListener('click', function (e) { e.stopPropagation(); n.classList.toggle('on'); });",
          "  document.addEventListener('click', function () { n.classList.remove('on'); });",
          "  document.addEventListener('keydown', function (e) {",
          "    if (e.key === 'Escape') n.classList.remove('on');",
          '  });', '})();', '</script>']
    return css + "\n".join(L) + "\n"


out = head + CSS + APP + "\n" + js + "\n" + JS2 + "\n" + docnav(OUT) + "</body>\n</html>\n"
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("%s  %d bytes  ch=%d  recent=%d" % (OUT, len(out.encode("utf-8")), NCH, len(RECENT)))
