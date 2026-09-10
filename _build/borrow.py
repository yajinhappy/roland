# -*- coding: utf-8 -*-
import io

p = "_build/ws2-w5.html"
h = io.open(p, encoding="utf-8").read()

OLD = '''          <span class="em-h2">미작성 화면 — 메뉴 정의 대비 화면 부재</span>
          <div class="bx">
            <table class="tbl">
              <thead><tr><th style="width:130px;">화면</th><th>필요한 것</th><th style="width:150px;">미결 사항</th></tr></thead>
              <tbody>
                <tr>
                  <td><b>구매내역</b></td>
                  <td>회원은 계정 기준 목록 · 비회원은 <b>주문번호 + 캐릭터 인증</b> 후 조회.
                    월 단위 조회 · 영수증 발급 · 결제 현황(구매 / 취소 / 실패 / 처리 중)</td>
                  <td class="bad-cell">비회원 조회 인증 방식 미정</td>
                </tr>
                <tr>
                  <td><b>FAQ</b></td>
                  <td>결제 · 지급 · 환불 문의 정리. 지사별로 내용이 다르다</td>
                  <td>콘텐츠 관리 주체 미정</td>
                </tr>
              </tbody>
            </table>
          </div>'''

NEW = '''          <span class="em-h2">미작성 화면 — 메뉴 정의 대비 화면 부재</span>
          <span class="ds2">화면은 미작성이나 <b>요건은 확보되어 있다.</b>
          기존 웹샵 화면정의서의 정의를 <b>단건 결제 · 수량 미적용 결정에 맞춰 조정</b>해 아래에 정리한다.</span>

          <div class="bx">
            <table class="tbl">
              <thead><tr><th style="width:130px;">화면</th><th>진입 경로</th><th style="width:170px;">미결 사항</th></tr></thead>
              <tbody>
                <tr><td><b>결제 완료</b></td><td>결제 페이지에서 결제 완료 후 <b>자동 복귀</b></td><td class="bad-cell">쿠폰 유효기간 · 사용 후 상태 표기</td></tr>
                <tr><td><b>구매내역</b></td><td>메뉴바 <b>[구매내역]</b> 탭</td><td class="bad-cell">비회원 조회 인증 방식 · 조회 가능 기간 상한</td></tr>
                <tr><td><b>FAQ</b></td><td>메뉴바 <b>[FAQ]</b> 탭</td><td>콘텐츠 관리 주체</td></tr>
              </tbody>
            </table>
          </div>

          <span class="tt2" style="margin-top:4px;">결제 완료 — 요건</span>
          <div class="bx">
            <table class="tbl">
              <thead><tr><th style="width:130px;">항목</th><th>회원</th><th>비회원</th></tr></thead>
              <tbody>
                <tr><td><b>완료 메시지</b></td><td>구매 아이템이 <b>게임 내 우편함으로 발송</b>되었습니다</td><td><b>쿠폰 번호가 발급</b>되었습니다. 게임에서 쿠폰을 등록해 수령해 주세요</td></tr>
                <tr><td><b>수령 방법</b></td><td>서버 검증 완료 즉시 <b>계정 우편함 자동 발송</b> · 수령 계정 마스킹 ID 표기 (캐릭터명 미표기)</td><td><b>쿠폰 1장</b> — 상품명 + 쿠폰 번호 + [복사]</td></tr>
                <tr><td><b>쿠폰 표기</b></td><td>—</td><td><b>4자리 × 4블록</b> <span class="mono">ABCD-1234-EFGH-5678</span> · 대문자 · 숫자 · <b>혼동 문자(O 0 I 1) 제외</b></td></tr>
                <tr><td><b>쿠폰 전달</b></td><td>—</td><td><b>이메일 동시 발송</b> · 화면 이탈 후 구매내역에서 재확인 · <b>1회 사용 · 재발급 불가</b></td></tr>
                <tr><td><b>보관 안내</b></td><td>미노출 — 주문이 계정에 귀속된다</td><td class="bad-cell"><b>강조 노출</b> — 쿠폰 · 주문번호 보관. 조회는 <b>주문번호 + 캐릭터 인증</b>으로만 가능</td></tr>
                <tr><td><b>주문 상세</b></td><td>주문번호 / 구매일시 / 상품 / 금액 / 결제수단 / <b>수령 방법(계정 우편함)</b></td><td>동일 항목 + <b>수령 캐릭터</b></td></tr>
                <tr><td><b>검증 지연</b></td><td colspan="2"><b>「처리 중」 상태 화면</b> 노출 후 완료 시 자동 갱신</td></tr>
                <tr><td><b>발송 실패</b></td><td>재발송 대상으로 표기 + 고객센터 안내</td><td>—</td></tr>
                <tr><td><b>액션</b></td><td colspan="2">[구매내역] · [상점으로 돌아가기] — <b>선택 상품 초기화</b></td></tr>
                <tr><td><b>결제 취소 시</b></td><td>—</td><td>미사용 쿠폰 <b>즉시 폐기</b> · 사용 완료 쿠폰은 취소 불가</td></tr>
              </tbody>
            </table>
          </div>

          <span class="tt2" style="margin-top:4px;">구매내역 — 요건</span>
          <div class="bx">
            <table class="tbl">
              <thead><tr><th style="width:130px;">항목</th><th>요건</th></tr></thead>
              <tbody>
                <tr><td><b>상단 구조</b></td><td>웹샵 메인과 <b>동일 배너 · 동일 위치</b> · 메뉴바에서 [구매내역]만 활성. 전용 배너를 별도 등록하지 않는다</td></tr>
                <tr><td><b>조회 기간</b></td><td><b>월 단위</b> <span class="mono">MM/YYYY</span> 선택 · 기본값 <b>당월</b> · 선택 시 목록 갱신 및 <b>1페이지로 초기화</b></td></tr>
                <tr><td><b>테이블 컬럼</b></td><td>No / 주문번호 / 구매 일시 / 구매 상품 / 구매 금액 / 영수증 / 결제 현황</td></tr>
                <tr><td><b>표기 규칙</b></td><td>No <b>최신 건 상단 · 내림차순 고정</b>(정렬 컨트롤 없음) · 구매 일시 <span class="mono">YYYY.MM.DD HH:MM</span>(초 미표기) · 금액은 <b>할인 적용 후</b></td></tr>
                <tr><td><b>결제 현황</b></td><td><b>구매 / 취소 / 결제 실패 / 처리 중</b> — 취소 건은 색으로 구분</td></tr>
                <tr><td><b>행 클릭</b></td><td><b>이동 없음</b> — 주문 상세 페이지를 두지 않고 목록에서 모두 노출한다</td></tr>
                <tr><td><b>영수증</b></td><td>행별 아이콘 클릭 시 <b>팝업(신규 창)</b> · 구성은 주문번호 · 일시 / 상품명 / 금액 · 결제수단 / 수령 정보 / 판매자 정보. <b>취소 · 실패 건은 비활성</b></td></tr>
                <tr><td><b>페이징</b></td><td><b>10건 · 10개 블록</b> · 처음 · 이전 · 번호 · 다음 · 마지막 · 양 끝에서 해당 컨트롤 비활성 · 이동 시 상단 스크롤</td></tr>
                <tr><td><b>조회 주체</b></td><td>회원은 <b>계정 기준</b> · 비회원은 <b>서버 + 캐릭터 인증 후</b> 해당 캐릭터 구매만. 인증 전에는 빈 상태 안내</td></tr>
                <tr><td><b>빈 상태</b></td><td>「구매 내역이 없습니다」</td></tr>
                <tr><td><b>MO</b></td><td>7컬럼 테이블 → <b>주문 1건 = 카드 1장</b> · 계정 인증은 <b>리스트 상단 가로 바</b> · 달력은 <b>바텀시트</b> · 페이징 <b>5개 블록</b></td></tr>
              </tbody>
            </table>
          </div>

          <div class="em-warn">
            <b>단건 결제 결정으로 폐기한 원안 항목</b> —
            기존 정의의 「아이템별 쿠폰 개별 발급」 · 「수량만큼 발급하고 <span class="mono">상품명 (1/2)</span> 표기」 ·
            「[전체 복사]」 · 「발급 10개 초과 시 스크롤」 · 「구매 상품 <span class="mono">대표 상품명 외 N건</span>」은
            <b>주문 1건 = 상품 1개 = 쿠폰 1장</b> 구조에서 발생하지 않는다.
            결제수단을 웹샵 위젯에서 선택하는 원안도 <b>결제 페이지 선택 방식으로 대체</b>되었다.
          </div>'''

assert OLD in h, "section1"
h = h.replace(OLD, NEW)

# 디스크립션 핀 1 갱신
OLD_ROW = '''        <p class="dr-b">메뉴바에 <b>구매내역 · FAQ</b>가 있는데 화면이 없다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">구매내역</span><span class="spec-v">비회원은 <b>계정이 없어</b> 주문번호와 캐릭터 인증으로 찾아야 한다 — 인증 방식을 정해야 한다</span></div>
          <div class="spec-r"><span class="spec-k">FAQ</span><span class="spec-v">지사마다 결제수단 · 환불 정책이 달라 <b>내용이 다르다</b> — 관리 주체를 정해야 한다</span></div>
          <div class="spec-r"><span class="spec-k">순서</span><span class="spec-v">구매내역이 먼저다 — <b>FAQ 없이도 팔 수 있지만</b> 구매내역 없이는 CS가 돌지 않는다</span></div>
        </div>'''
NEW_ROW = '''        <p class="dr-b"><b>결제 완료 · 구매내역 · FAQ</b> 3개 화면이 미작성이다. 요건은 기존 화면정의서에서 확보했다.</p>
        <div class="spec">
          <div class="spec-r"><span class="spec-k">결제 완료</span><span class="spec-v">회원 <b>우편함 발송</b> / 비회원 <b>쿠폰 1장</b> 분기. 결제 페이지에서 복귀하는 화면이므로 <b>착수 우선순위 1</b></span></div>
          <div class="spec-r"><span class="spec-k">구매내역</span><span class="spec-v">비회원은 계정이 없어 <b>주문번호 + 캐릭터 인증</b>으로 조회한다 — 인증 방식 확정 필요</span></div>
          <div class="spec-r"><span class="spec-k">FAQ</span><span class="spec-v">법인별 결제수단 · 환불 정책이 상이하므로 <b>내용이 다르다</b> — 관리 주체 확정 필요</span></div>
          <div class="spec-r"><span class="spec-k">착수 순서</span><span class="spec-v">결제 완료 &rarr; 구매내역 &rarr; FAQ. <b>FAQ 없이 운영 가능하나</b> 앞의 둘 없이는 CS 대응이 불가하다</span></div>
          <div class="spec-r"><span class="spec-k">조정 사항</span><span class="spec-v">원안의 쿠폰 분할 발급 · 다건 요약 표기는 <b>단건 결정으로 미해당</b></span></div>
        </div>'''
assert OLD_ROW in h, "row1"
h = h.replace(OLD_ROW, NEW_ROW)

io.open(p, "w", encoding="utf-8", newline="\n").write(h)
io.open("_ok.txt", "w", encoding="utf-8").write("borrowed into w5 section 1")
