# -*- coding: utf-8 -*-
import io

GLOBE = ('<svg class="ico" viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" fill="none" '
         'stroke="currentColor" stroke-width="1.5"><circle cx="10" cy="10" r="7.2"/><path d="M2.8 10h14.4"/>'
         '<path d="M10 2.8c1.9 2 2.9 4.5 2.9 7.2s-1 5.2-2.9 7.2c-1.9-2-2.9-4.5-2.9-7.2S8.1 4.8 10 2.8z"/></svg>')
MAG = ('<svg class="ico" viewBox="0 0 20 20" width="16" height="16" aria-hidden="true">'
       '<circle cx="8.5" cy="8.5" r="5.6" fill="none" stroke="currentColor" stroke-width="1.7"/>'
       '<path d="M12.8 12.8 L17.6 17.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>')

def util(kind, member=False):
    """kind: pc | tb | mo"""
    who = "내 정보" if member else "로그인"
    if kind == "pc":
        return '''          <div class="ws-host" style="position:relative;">
            <span class="ws-hostlbl">HOST — 웹샵 모듈 아님</span>
            <div class="wrapc ws-util">
              <div class="img" style="width:190px;height:34px;"><span class="sp">RAGNAROK PORTAL 로고<br>SVG</span></div>
              <span class="lang" style="margin-left:auto;">%s KO <span style="font-size:9px;">&#9662;</span></span>
              <span style="width:1px;height:16px;background:#DCE2E8;"></span>
              <div class="srch" style="display:flex;align-items:center;gap:6px;">%s<span class="ts">SEARCH</span></div>
              <span class="ts">%s</span>
            </div>
          </div>''' % (GLOBE, MAG, who)
    if kind == "tb":
        return '''              <div class="ws-host" style="border-radius:0;border:0;">
                <div class="ws-util tb">
                  <div class="img" style="width:150px;height:28px;"><span class="sp" style="font-size:8.5px;">PORTAL 로고</span></div>
                  <span class="lang" style="margin-left:auto;">KO <span style="font-size:9px;">&#9662;</span></span>
                  <span style="width:1px;height:14px;background:#DCE2E8;"></span>
                  <span class="ts">SEARCH</span>
                  <span class="ts">%s</span>
                </div>
              </div>''' % who
    return '''              <div class="ws-host" style="border-radius:0;border:0;">
                <div class="ws-util mo">
                  <div class="img" style="width:110px;height:22px;"><span class="sp" style="font-size:8px;">PORTAL 로고</span></div>
                  <span class="lang" style="margin-left:auto;">KO <span style="font-size:9px;">&#9662;</span></span>
                  <span class="ts">%s</span>
                </div>
              </div>''' % who

def banner(kind):
    if kind == "pc":
        return '''            <div class="ws-title">
              <span class="ws-kvsafe"></span>
              <span class="ws-kvnote">키비주얼 배너 1440 × 280</span>
              <div class="ws-kvin">
                <span class="ws-glogo">게임<br>로고</span>
                <div><span class="ws-kvh">라그나로크 어비스</span><span class="ws-kvs">WEBSHOP</span></div>
              </div>
            </div>'''
    if kind == "tb":
        return '''                <div class="ws-title tb">
                  <span class="ws-kvnote">1536 × 460</span>
                  <div class="ws-kvin">
                    <span class="ws-glogo">게임<br>로고</span>
                    <div><span class="ws-kvh">라그나로크 어비스</span><span class="ws-kvs">WEBSHOP</span></div>
                  </div>
                </div>'''
    return '''                <div class="ws-title mo">
                  <span class="ws-kvnote">750 × 300</span>
                  <div class="ws-kvin">
                    <span class="ws-glogo">게임<br>로고</span>
                    <div><span class="ws-kvh">라그나로크 어비스</span><span class="ws-kvs">WEBSHOP</span></div>
                  </div>
                </div>'''

def menu(kind, active):
    cur = ''
    def cls(n): return ' class="ws-mi on"' if n == active else ' class="ws-mi"'
    if kind == "pc":
        return ('            <div class="ws-menu">\n'
                '              <span%s>상품구매</span>\n'
                '              <span%s>구매내역</span>\n'
                '              <span%s>FAQ</span>\n'
                '              %s\n'
                '            </div>') % (cls("buy"), cls("hist"), cls("faq"), cur)
    if kind == "tb":
        def c2(n): return ' class="on"' if n == active else ''
        return ('                <div class="ws-tbmenu">\n'
                '                  <span%s>상품구매</span><span%s>구매내역</span><span%s>FAQ</span>\n'
                '                  %s\n'
                '                </div>') % (c2("buy"), c2("hist"), c2("faq"), cur)
    def c3(n): return ' class="on"' if n == active else ''
    return ('                <div class="ws-mmenu">\n'
            '                  <span%s>상품구매</span><span%s>구매내역</span><span%s>FAQ</span>\n'
            '                </div>') % (c3("buy"), c3("hist"), c3("faq"))

# ═══════════════════════════════════════════ 결제 완료 본문
def cp_body(guest, kind="pc"):
    mk = lambda n, pos: '<div class="mk" style="position:absolute;%s">%d</div>' % (pos, n)
    ico = '<span class="cp-ico">&#10003;</span>'
    if guest:
        msg = '쿠폰 번호가 발급되었습니다'
        sub = '게임에서 쿠폰을 등록해 아이템을 수령해 주세요'
        recv = '''            <div class="cp-card">
              %s
              <div class="cp-ch">수령 방법 — 쿠폰 번호</div>
              <div class="cp-cb">
                <div class="cp-coup">
                  <span class="nm3">프리미엄 성장석</span>
                  <span class="cd">ABCD-1234-EFGH-5678</span>
                  <span class="btn-s" style="flex:none;">복사</span>
                </div>
                <div class="cp-mail"><b>&#9993;</b> 쿠폰 번호를 이메일로도 발송했습니다</div>
                <span class="tg-hint"><em>i</em>표기 <b>4자리 × 4블록</b> · 대문자 · 숫자 · 혼동 문자(O 0 I 1) 제외 · <b>1회 사용 · 재발급 불가</b></span>
              </div>
            </div>''' % mk(2, 'top:12px;left:-33px;')
        keep = '''            <div class="cp-card" style="border-color:#E2D5B9;">
              %s
              <div class="cp-cb" style="padding:0;">
                <div class="cp-keep">
                  <b>쿠폰 번호와 주문번호를 보관해 주세요.</b><br>
                  주문이 계정에 귀속되지 않아 <b>쿠폰 번호는 재발급되지 않습니다.</b>
                  구매내역 조회는 <b>주문번호 + 캐릭터 인증</b>으로만 가능합니다.
                </div>
              </div>
            </div>''' % mk(3, 'top:12px;left:-33px;')
        detail_last = '<div class="cp-dr"><span class="k2">수령 캐릭터</span><span class="v2"><b>발할라 / 프론테라기사</b></span></div>'
    else:
        msg = '구매하신 아이템이 게임 내 우편함으로 발송되었습니다'
        sub = '게임에 접속해 우편함에서 수령해 주세요'
        recv = '''            <div class="cp-card">
              %s
              <div class="cp-ch">수령 방법 — 계정 우편함</div>
              <div class="cp-cb">
                <div class="cp-mail"><b>&#9993;</b> 게임 내 <b>계정 우편함 발송 완료</b> — <span class="mono">ro_ab***@gnjoy</span></div>
                <span class="tg-hint"><em>i</em>수령 계정만 표기하고 <b>캐릭터명은 표기하지 않는다</b> · 별도 등록 절차 없음</span>
                <span class="tg-hint"><em>i</em>우편 보관 기간 · 미수령 처리는 <b>게임 우편 정책</b>을 따른다</span>
              </div>
            </div>''' % mk(2, 'top:12px;left:-33px;')
        keep = ''
        detail_last = '<div class="cp-dr"><span class="k2">수령 방법</span><span class="v2"><b>계정 우편함</b></span></div>'

    detail = '''            <div class="cp-card">
              %s
              <div class="cp-ch">주문 상세</div>
              <div class="cp-cb" style="gap:0;">
                <div class="cp-dr"><span class="k2">주문번호</span><span class="v2 mono">20260908-000482</span></div>
                <div class="cp-dr"><span class="k2">구매일시</span><span class="v2 mono">2026.09.08 14:32</span></div>
                <div class="cp-dr"><span class="k2">상품</span><span class="v2">프리미엄 성장석</span></div>
                <div class="cp-dr"><span class="k2">결제 금액</span><span class="v2 mono">₩ 4,900</span></div>
                <div class="cp-dr"><span class="k2">결제수단</span><span class="v2">신용카드 신한 · 일시불</span></div>
                %s
              </div>
            </div>''' % (mk(4, 'top:12px;left:-33px;'), detail_last)

    act = '''            <div class="cp-act" style="position:relative;">
              %s
              <span class="s">구매내역</span>
              <span class="p">상점으로 돌아가기</span>
            </div>''' % mk(5, 'top:14px;left:-33px;')

    parts = ['            <div style="position:relative;display:flex;flex-direction:column;gap:10px;align-items:center;">',
             '              ' + mk(1, 'top:8px;left:-33px;'),
             '              ' + ico,
             '              <span class="cp-msg">%s</span>' % msg,
             '              <span class="cp-sub">%s</span>' % sub,
             '            </div>',
             recv]
    if keep:
        parts.append(keep)
    parts += [detail, act]
    return "\n".join(p for p in parts if p)

# ═══════════════════════════════════════════ 구매내역 본문
HS_ROWS = [
    ("1", "20260908-000482", "2026.09.08 14:32", "프리미엄 성장석", "₩ 4,900", "on", "구매"),
    ("2", "20260906-000311", "2026.09.06 21:07", "축제 의상 세트", "₩ 7,500", "on", "구매"),
    ("3", "20260903-000107", "2026.09.03 10:18", "고급 스킬북", "₩ 3,200", "off", "취소"),
    ("4", "20260901-000042", "2026.09.01 19:44", "여름 한정 소환석", "₩ 12,000", "off", "결제 실패"),
]

def hs_table():
    body = []
    for no, od, dt, nm, pr, rc, st in HS_ROWS:
        tag = 'tag-g' if st == "구매" else ('tag-n' if st == "취소" else 'tag-r')
        body.append('                  <tr><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td>'
                    '<td>%s</td><td class="pr">%s</td>'
                    '<td><span class="hs-rc%s">&#128441;</span></td>'
                    '<td><span class="%s">%s</span></td></tr>'
                    % (no, od, dt, nm, pr, ("" if rc == "on" else " off"), tag, st))
    return ('''              <table class="hs-tbl">
                <thead><tr><th style="width:42px;">No</th><th style="width:132px;">주문번호</th>
                  <th style="width:126px;">구매 일시</th><th>구매 상품</th>
                  <th style="width:88px;">구매 금액</th><th style="width:58px;">영수증</th>
                  <th style="width:82px;">결제 현황</th></tr></thead>
                <tbody>
%s
                </tbody>
              </table>''' % "\n".join(body))

HS_PG = '''              <div class="hs-pg">
                <span class="dis">|&#9664;</span><span class="dis">&#9664;</span>
                <span class="on">1</span><span>2</span><span>3</span>
                <span>&#9654;</span><span>&#9654;|</span>
              </div>'''

def hs_auth(guest):
    if guest:
        return '''            <div class="ws-card">
              <div class="mk" style="position:absolute;top:10px;right:-33px;">6</div>
              <div class="ws-ch"><b>계정 인증</b><span class="tag" style="margin-left:auto;">비회원</span></div>
              <div class="ws-cb">
                <div class="fld">
                  <span class="lbl-k">서버</span>
                  <div class="inp"><span style="font-size:12px;color:#98A2AE;">서버 선택</span>
                    <span style="margin-left:auto;font-size:9px;color:#6C7480;">&#9662;</span></div>
                </div>
                <div class="fld">
                  <span class="lbl-k">캐릭터 ID</span>
                  <div class="inp"><span style="font-size:12px;color:#98A2AE;">캐릭터 ID 입력</span></div>
                </div>
                <span class="btn-w">인증</span>
                <span class="tg-hint"><em>i</em>인증한 캐릭터로 구매한 내역만 조회됩니다</span>
              </div>
            </div>'''
    return '''            <div class="ws-card">
              <div class="mk" style="position:absolute;top:10px;right:-33px;">6</div>
              <div class="ws-ch"><b>계정 인증</b><span class="tag" style="margin-left:auto;">회원</span></div>
              <div class="ws-cb">
                <div class="tg-done">
                  <span class="ck">&#10003;</span>
                  <span class="nmv">계정 인증 완료 · <b>ro_ab***@gnjoy</b></span>
                </div>
                <span class="tg-hint"><em>i</em>계정에 귀속된 구매를 <b>선택 월 기준 최신순</b>으로 노출합니다</span>
              </div>
            </div>'''

io.open("_build/_gen67.txt", "w", encoding="utf-8").write("helpers loaded")
