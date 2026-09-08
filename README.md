# 라그나로크 포털 기획 문서

사내 열람용 정적 문서 사이트. `index.html`을 열면 전체 문서 목록이 나온다.

## 문서 구성

### 화면정의서

| 파일 | 문서명 |
|---|---|
| `wireframe/portal-main-auth-screens.html` | 라그나로크 포털 화면정의서 |
| `wireframe/webshop-ui.html` | **웹샵 UI 구성** — 7 탭 · 핀 43건 |
| `wireframe/payment-checkout-currency.html` | 통합 결제창 화면정의서 |
| `wireframe/payment-admin-screens.html` | 결제 관리자 화면정의서 — 9 화면 · 핀 55건 |

### 설계

| 파일 | 문서명 |
|---|---|
| `wiki/planning/portal-main-structure.html` | 포털 메인 구조 |
| `wiki/planning/land-auth.html` | 랜드 회원·인증 설계 |
| `wiki/planning/payment.html` | 결제 설계 — 프로세스 · 구조 |
| `wiki/planning/payment-webshop-structure.html` | **통합결제 / 웹샵 구조** |
| `wiki/planning/global-payment.html` | 글로벌 결제 설계 (상세) |

### 벤치마킹

| 파일 | 문서명 |
|---|---|
| `wiki/benchmark/ip-portal.html` | IP 포털 벤치마킹 |
| `wiki/benchmark/nc-auth.html` | NC 회원·인증 통합 벤치마킹 |
| `wiki/benchmark/pg-multi-entity.html` | PG 다중법인 구조 벤치마킹 |
| `wiki/benchmark/game-platform-payment.html` | 게임 플랫폼 결제 구조 벤치마킹 |
| `wiki/benchmark/webshop-payment.html` | 웹샵 결제 벤치마킹 |

### 목록에는 없고 본문 링크로만 연결

| 파일 | 문서명 |
|---|---|
| `wiki/planning/payment-overview.html` | 결제 개요 — 1장 |
| `wireframe/payment-user-screens.html` | 통합 결제 페이지 화면정의서 |

## 확정된 설계 전제

| 항목 | 내용 |
|---|---|
| 제공 구성 | 본사가 **웹샵 템플릿 · 통합 결제 페이지 · 관리자** 3종을 제공하고 지사가 가져다 쓴다 |
| 임베드 | **SDK 삽입 + Shadow DOM** · 오버레이는 body 직속 레이어 |
| 법인 판정 | **등록 도메인(Origin)** 기준으로 서버가 판정 · 프론트엔드 전달값 불신 |
| 자금 · 매출 | PG 계약 명의가 지사이므로 **대금이 해당 법인 계좌로 직접 입금** · 본사 미경유 |
| 거래 단위 | **주문 1건 = 상품 1개 = 지급 1회 = 환불 1회** · 수량 · 장바구니 미적용 |
| 상품 범위 | 웹샵은 **캐릭터 기반**만 · 계정 기반 · 구독은 **지사 포털** 기본 |
| 수령 | **계정 우편함 발송** 단일 흐름 (쿠폰 방식 폐기) |
| 통화 | 법인당 복수 · 웹샵은 표시만 하고 **선택은 통합 결제창**에서 |
| PC 콘텐츠 폭 | 최대 **1600** · 배너 핵심 요소는 중앙 **1400** |

## 빌드

문서는 `_build/`의 조립 재료로 생성한다. **`_build/`는 배포 대상이 아니다.**

| 스크립트 | 대상 |
|---|---|
| `_build/gen_nav.py` | 문서 목록 단일 소스. NAV 수정 후 아래 빌드를 다시 실행 |
| `_build/build_v2.py` | 결제 개요 · 결제 설계 · 통합결제/웹샵 구조 |
| `_build/build_ws.py` | 웹샵 UI 구성 |

### 검증

| 스크립트 | 확인 항목 |
|---|---|
| `_build/linkcheck.js` | 내부 링크 · 절대경로 · 끊긴 링크 |
| `_build/wscheck.js` | 웹샵 UI 구성 — 화면 · 탭 · 순서 일치, 핀↔설명 대응 |
| `_build/finalcheck.py` | 전 문서 태그 균형 · 미정의 클래스 |

## 구조

```
index.html            문서 목록
wiki/planning/        설계
wiki/benchmark/       벤치마킹
wireframe/            화면정의서
_build/               조립 재료 (배포 제외)
```
