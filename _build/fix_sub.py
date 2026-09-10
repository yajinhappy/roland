# -*- coding: utf-8 -*-
import io

p = "_build/ws2-w5.html"
h = io.open(p, encoding="utf-8").read()

# ── 캔버스 : 구독 섹션 본문 교체 ──
old_lead = '''          <span class="ds2">구독은 <b>반복 결제</b>라 지금 구조로 덮이지 않는다.
          계정 축과는 무관한 별개 과제이고, <b>도입 전에 아래가 정해져야 한다.</b>
          포인트는 1회 결제이므로 이 문제가 없고, <b>정액제도 기간제면 같은 문제</b>다.</span>'''
new_lead = '''          <span class="ds2">구독은 <b>반복 결제 기능을 신규 구현</b>하는 과제다.
          아래 항목 대부분은 <b>구독 서비스의 일반 요건</b>이며, 본 구조에서 별도 검토가 필요한 것은 <b>1건</b>이다.
          포인트는 1회 결제이므로 해당되지 않고, <b>정액제도 기간제로 구성하면 동일 범위</b>다.</span>'''
assert old_lead in h, "lead"
h = h.replace(old_lead, new_lead)

old_tbl = '''              <thead><tr><th style="width:150px;">항목</th><th>왜 문제인가</th><th style="width:170px;">확정 필요 사항</th></tr></thead>
              <tbody>
                <tr>
                  <td><b>갱신 시점 판정</b></td>
                  <td>갱신은 유저 조작 없이 서버가 자동 청구한다 — <b>도메인 판정이 없다</b></td>
                  <td class="bad-cell">최초 결제 때 지사 · 통화 · 결제수단을 <b>고정</b>해 계속 쓴다</td>
                </tr>
                <tr>
                  <td><b>결제수단 저장</b></td>
                  <td>정기결제에는 <b>빌링키</b>가 필요하다. 간편결제 · 통신사 결제는 <b>지원하지 않는 경우</b>가 있다</td>
                  <td class="bad-cell">PG · 결제수단별 정기결제 지원 여부 확인</td>
                </tr>
                <tr>
                  <td><b>갱신 실패</b></td>
                  <td>카드 만료 · 한도 초과로 실패한다</td>
                  <td>재시도 횟수 · <b>유예 기간</b> · 권한 회수 시점</td>
                </tr>
                <tr>
                  <td><b>해지 · 환불</b></td>
                  <td>남은 기간을 일부 환불하면 <b>부분취소</b> 문제로 돌아온다</td>
                  <td>일할 환불 여부 · 안 하면 <b>기간 만료까지 유지</b></td>
                </tr>
                <tr>
                  <td><b>가격 변경</b></td>
                  <td>구독 중 가격이 바뀌면 기존 구독자에게 적용할지</td>
                  <td>사전 고지 기간 · 기존 가격 유지 여부</td>
                </tr>
                <tr>
                  <td><b>통화 고정</b></td>
                  <td>통화를 고정하면 장기 구독의 <b>환율 변동을 지사가 흡수</b>한다</td>
                  <td>중간 변경 허용 여부</td>
                </tr>
                <tr>
                  <td><b>법정 고지</b></td>
                  <td>정기결제는 국가마다 <b>사전 고지 · 해지 편의 의무</b>가 다르다</td>
                  <td class="bad-cell">지사별 법무 확인</td>
                </tr>
                <tr>
                  <td><b>정산 대사</b></td>
                  <td>갱신 건은 <b>웹샵을 거치지 않는다</b> — 대사 기준이 일반 결제와 다르다</td>
                  <td>갱신 건 식별 · 대사 방식</td>
                </tr>
              </tbody>'''

new_tbl = '''              <thead><tr><th style="width:74px;">구분</th><th style="width:150px;">항목</th><th>내용</th><th style="width:170px;">확정 필요 사항</th></tr></thead>
              <tbody>
                <tr>
                  <td><span class="tag-r">구조</span></td>
                  <td><b>갱신 시점 법인 판정</b></td>
                  <td>웹샵은 <b>도메인으로 법인을 판정</b>한다. 갱신은 사용자 조작 없이 서버가 청구하므로 판정 근거가 없다.
                    <b>지사 포털에서 판매하면 계정이 법인을 확정하므로 해당되지 않는다</b></td>
                  <td class="bad-cell">웹샵 판매 시 최초 결제의 법인 · 통화 · 결제수단을 <b>세션에 고정</b></td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>결제수단 저장</b></td>
                  <td>정기결제에는 <b>빌링키</b>가 필요하다. 간편결제 · 통신사 결제는 미지원 사례가 있다</td>
                  <td>PG · 결제수단별 정기결제 지원 여부</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>갱신 실패</b></td>
                  <td>카드 만료 · 한도 초과 시 실패한다</td>
                  <td>재시도 횟수 · 유예 기간 · 권한 회수 시점</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>해지 · 환불</b></td>
                  <td>잔여 기간 일할 환불은 <b>부분취소</b>에 해당한다</td>
                  <td>일할 환불 여부 · 미적용 시 기간 만료까지 유지</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>가격 변경</b></td>
                  <td>구독 중 가격 변경 시 기존 구독자 적용 범위</td>
                  <td>사전 고지 기간 · 기존 가격 유지 여부</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>통화 고정</b></td>
                  <td>통화 고정 시 장기 구독의 환율 변동을 법인이 흡수한다</td>
                  <td>중간 변경 허용 여부</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>법정 고지</b></td>
                  <td>정기결제 사전 고지 · 해지 편의 의무가 국가별로 상이하다</td>
                  <td>법인별 법무 확인</td>
                </tr>
                <tr>
                  <td><span class="tag-n">일반</span></td>
                  <td><b>정산 대사</b></td>
                  <td>갱신 건은 판매 화면을 경유하지 않아 대사 기준이 일반 결제와 다르다</td>
                  <td>갱신 건 식별 · 대사 방식</td>
                </tr>
              </tbody>'''
assert old_tbl in h, "table"
h = h.replace(old_tbl, new_tbl)

old_warn = '''          <div class="em-warn">
            <b>현 결정</b> — 구독은 <b>현 범위에 넣지 않는다.</b>
            위 8건이 정해지기 전에는 화면을 그려도 규격이 바뀐다.
            정액제를 먼저 넣어야 하면 <b>기간제 대신 1회성 아이템</b>으로 다루는 방법도 있다 —
            30일 이용권을 <b>구독이 아니라 소비 아이템</b>으로 팔면 반복 결제가 사라진다.
          </div>'''
new_warn = '''          <div class="em-warn">
            <b>현 결정</b> — 구독은 <b>현 범위에 넣지 않는다.</b>
            구조상 막히는 것이 아니라 <b>반복 결제 기능 일체를 신규 구현</b>해야 하므로 별도 과제로 분리한다.
            판매 채널로는 <b>지사 포털이 적합</b>하다 — 로그인이 전제이므로 갱신 시 법인 판정 문제가 발생하지 않는다.
            정액제만 선행 도입할 경우 30일 이용권을 <b>구독이 아닌 소비 아이템</b>으로 등록하면 반복 결제 없이 판매 가능하다.
          </div>'''
assert old_warn in h, "warn"
h = h.replace(old_warn, new_warn)

# ── 디스크립션 : 핀 7 행 교체 ──
old_row = '''        <p class="dr-b"><b>반복 결제</b>가 지금 구조로 덮이지 않는다. 8건이 정해지기 전에는 화면을 그려도 규격이 바뀐다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">주요 사항</span><span class="spec-v">갱신은 <b>도메인 판정이 없다</b> — 최초 결제 때 지사 · 통화 · 결제수단을 고정해야 한다</span></div>
          <div class="spec-r"><span class="spec-k">제약 가능 항목</span><span class="spec-v"><b>빌링키</b> — 간편결제 · 통신사 결제는 정기결제를 지원하지 않는 경우가 있다</span></div>
          <div class="spec-r"><span class="spec-k">연쇄 영향</span><span class="spec-v">해지 시 일할 환불 &rarr; <b>부분취소</b> 문제. 안 하면 기간 만료까지 유지</span></div>
          <div class="spec-r"><span class="spec-k">대안</span><span class="spec-v">30일 이용권을 <b>구독이 아니라 소비 아이템</b>으로 팔면 반복 결제가 사라진다</span></div>
          <div class="spec-r"><span class="spec-k">현 범위</span><span class="spec-v"><b>범위 밖</b> — 정액제 · 구독을 넣기로 하면 이 표부터 확정한다</span></div>
        </div>'''
new_row = '''        <p class="dr-b"><b>반복 결제 기능의 신규 구현</b> 과제다. 구조상 막히는 항목은 <b>1건</b>이고 나머지는 일반 요건이다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">구조 항목</span><span class="spec-v"><b>갱신 시점 법인 판정</b> 1건 — 웹샵은 도메인 판정 방식이라 갱신 시 근거가 없다</span></div>
          <div class="spec-r"><span class="spec-k">해소 조건</span><span class="spec-v"><b>지사 포털 판매 시 해당되지 않는다</b> — 로그인 계정이 법인을 확정한다</span></div>
          <div class="spec-r"><span class="spec-k">일반 요건</span><span class="spec-v">빌링키 · 갱신 실패 · 해지 환불 · 가격 변경 · 통화 고정 · 법정 고지 · 정산 대사 <b>7건</b></span></div>
          <div class="spec-r"><span class="spec-k">대안</span><span class="spec-v">30일 이용권을 <b>구독이 아닌 소비 아이템</b>으로 등록하면 반복 결제 없이 판매 가능</span></div>
          <div class="spec-r"><span class="spec-k">현 범위</span><span class="spec-v"><b>범위 외</b> — 구현 규모 때문이며 구조 제약 때문이 아니다</span></div>
        </div>'''
assert old_row in h, "row"
h = h.replace(old_row, new_row)

io.open(p, "w", encoding="utf-8", newline="\n").write(h)
io.open("_ok.txt", "w", encoding="utf-8").write("w5 subscription section corrected")
