# -*- coding: utf-8 -*-
import io

def sheet(label, inner, hh=560, member=False):
    return '''          <div class="tg-cell">
            <span class="tg-lbl"><em>%s</em></span>
            <div class="ws-tb" style="height:%dpx;">
              <div class="ws-util tb">
                <div class="img" style="width:150px;height:28px;"><span class="sp" style="font-size:8.5px;">PORTAL 로고</span></div>
                <span class="lang" style="margin-left:auto;">KO <span style="font-size:9px;">&#9662;</span></span>
                <span style="width:1px;height:14px;background:#DCE2E8;"></span>
                <span class="ts">SEARCH</span>
                <span class="ts">%s</span>
              </div>
              <div class="mo-body">
                <div class="scrim" style="align-items:flex-end;justify-content:center;">
                  <div class="tb-sheet">
                    <span class="mo-grip"></span>
                    <span class="mo-h" style="font-size:13.5px;">받을 캐릭터</span>
%s
                  </div>
                </div>
              </div>
            </div>
          </div>
''' % (label, hh, "내 정보" if member else "로그인", inner)

MONO = "font-family:'IBM Plex Mono',monospace;"

A1 = '''                    <div class="tg-login">
                      <p>로그인하면 <b>내 캐릭터를 바로 선택</b>할 수 있습니다</p>
                      <span class="tg-btn" style="width:260px;">로그인</span>
                    </div>
                    <div class="tg-or"><i></i><b>또는 캐릭터 인증으로 구매</b><i></i></div>
                    <div class="tb-2col">
                      <div class="fld">
                        <span class="lbl-k">서버</span>
                        <div class="inp mo"><span style="font-size:12.5px;color:#98A2AE;">서버 선택</span>
                          <span style="margin-left:auto;font-size:9px;color:#6C7480;">&#9662;</span></div>
                      </div>
                      <div class="fld">
                        <span class="rowk"><span class="lbl-k">캐릭터 ID</span>
                          <span class="tg-hint q" style="margin-left:auto;"><em>?</em>확인 방법</span></span>
                        <div style="display:flex;gap:7px;">
                          <div class="inp mo" style="flex:1;"><span style="font-size:12.5px;color:#98A2AE;">캐릭터 ID 입력</span></div>
                          <span class="btn-s" style="flex:none;white-space:nowrap;">인증번호 발송</span>
                        </div>
                      </div>
                    </div>
                    <div class="fld" style="max-width:360px;">
                      <span class="lbl-k">인증번호</span>
                      <div style="display:flex;gap:7px;">
                        <div class="inp mo dis" style="flex:1;"><span style="font-size:12.5px;">6자리 숫자</span></div>
                        <span class="btn-s" style="flex:none;">확인</span>
                      </div>
                      <span class="tg-hint"><em>i</em>인증번호는 <b>인게임 우편함</b>으로 전송됩니다</span>
                    </div>
                    <div class="ws-pay off" style="padding:12px 0;font-size:13px;">결제하기</div>'''

A3 = '''                    <div class="tg-done">
                      <span class="ck">&#10003;</span>
                      <span class="nmv">발할라 / <b>프론테라기사</b></span>
                      <span class="tg-x">&#10005;</span>
                    </div>
                    <span class="tg-hint"><em>i</em>구매한 아이템은 <b>이 캐릭터</b>로 지급됩니다</span>
                    <div style="display:flex;align-items:center;gap:18px;padding-top:10px;border-top:1px solid #E4E8ED;">
                      <span style="font-size:11.5px;color:#6C7480;">총 결제 금액</span>
                      <span style="font-size:18px;font-weight:600;color:#171B22;''' + MONO + '''margin-left:auto;">₩ 11,300</span>
                      <div class="ws-pay" style="width:240px;flex:none;padding:12px 0;">결제하기</div>
                    </div>'''

B1 = '''                    <div class="tb-2col">
                      <div class="fld">
                        <span class="lbl-k">서버</span>
                        <div class="inp mo"><span style="font-size:12.5px;color:#171B22;">발할라</span>
                          <span style="margin-left:auto;font-size:9px;color:#6C7480;">&#9662;</span></div>
                      </div>
                      <div class="fld">
                        <span class="lbl-k">캐릭터</span>
                        <div class="inp mo"><span style="font-size:12.5px;color:#171B22;">프론테라기사</span>
                          <span style="font-size:11px;color:#6C7480;margin-left:6px;">Lv.87 · 나이트</span>
                          <span style="margin-left:auto;font-size:9px;color:#6C7480;">&#9662;</span></div>
                      </div>
                    </div>
                    <span class="tg-hint"><em>i</em>인증 절차 없음 — 내 캐릭터만 보입니다</span>
                    <div class="ws-pay" style="padding:12px 0;font-size:13px;">결제하기</div>'''

T = '''                    <div class="tb-2col">
                      <div class="fld">
                        <span class="rowk"><span class="lbl-k">캐릭터 ID</span>
                          <span class="tg-hint q" style="margin-left:auto;"><em>?</em>확인 방법</span></span>
                        <div class="inp mo"><span style="font-size:12.5px;color:#98A2AE;">캐릭터 ID 입력</span></div>
                      </div>
                      <div class="tg-tipbox" style="position:static;width:auto;">
                        <b>캐릭터 ID는 어디서 보나요</b>
                        <ol>
                          <li>게임에 접속합니다</li>
                          <li>캐릭터 정보 창을 엽니다</li>
                          <li>캐릭터명 아래 <b>영문 ID</b>가 캐릭터 ID입니다</li>
                        </ol>
                        <div class="img" style="height:74px;"><span class="sp">확인 위치 이미지</span></div>
                      </div>
                    </div>
                    <span class="tg-hint"><em>i</em>태블릿은 <b>팝오버</b>로 띄운다 — MO만 바텀시트</span>'''

TB4 = ('''      <!-- ═══════════════ TABLET 768 ═══════════════ -->
      <div class="pane pane-tb">
      <div class="wstage">
      <div class="pcframe" style="display:flex;flex-direction:column;position:relative;">

        <div class="tg-tbwrap">
'''
+ sheet("A1  비로그인 진입 — 필드 2열", A1, 600)
+ sheet("A3  비회원 인증 완료", A3, 470)
+ sheet("B1  로그인 · 여러 개", B1, 470, member=True)
+ sheet("T  캐릭터 ID 확인 — 팝오버", T, 520)
+ '''        </div>

      </div>
      </div>
      </div>

''')

p = "_build/ws2-w4.html"
h = io.open(p, encoding="utf-8").read()
old = '''        <button type="button" class="tab tab-on" data-dev="pc">PC</button>
        <button type="button" class="tab" data-dev="mo">MO</button>'''
new = '''        <button type="button" class="tab tab-on" data-dev="pc">PC</button>
        <button type="button" class="tab" data-dev="tb">TABLET</button>
        <button type="button" class="tab" data-dev="mo">MO</button>'''
assert old in h, "w4 tabs"
h = h.replace(old, new, 1)
anchor = '      <!-- ═══════════════ MO — 상태 매트릭스 ═══════════════ -->'
assert anchor in h, "w4 mo anchor"
h = h.replace(anchor, TB4 + anchor, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(h)
io.open("_ok.txt", "w", encoding="utf-8").write("w4 tablet inserted")
