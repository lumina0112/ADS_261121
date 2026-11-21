---
version: 0.1
updated: 2026-11-21
name: kkal-clay-block
base: Clay DESIGN.md + Figma DESIGN.md (getdesign.md) 변형본
description: "차가운 흰 바탕(#FBFBFB)에 초록빛 먹색 글자를 쓰고, 잔 모듈 다섯 색(숲, 밤, 노을, 여울, 들)을 Clay식 색 카드로 칠한다. 구역은 Figma식 색 블록과 흰 바탕을 번갈아 두어 나눈다. 모듈 색은 모듈을 가리킬 때만 쓰고, 버튼과 링크는 먹색 알약으로 통일한다. 한글은 Pretendard Variable, 워드마크와 영문 라벨은 Unbounded로 쓴다."

colors:
  canvas: "#FBFBFB"
  surface-soft: "#F0F2F1"
  ink: "#1D2624"
  muted: "#57625F"
  on-dark: "#FBFBFB"
  hairline: "rgba(29,38,36,.12)"
  module:
    soop:  { hex: "#265F56", text: on-dark }   # 숲
    bam:   { hex: "#6F3C66", text: on-dark }   # 밤
    noeul: { hex: "#F15B5C", text: ink }       # 노을
    yeoul: { hex: "#9ED7E0", text: ink }       # 여울
    deul:  { hex: "#F7F2C5", text: ink, edge: hairline }   # 들

typography:
  fonts:
    text: "Pretendard Variable (jsDelivr). 한글 제목과 모든 본문."
    latin-display: "Unbounded (Google Fonts, OFL). 워드마크 KKAL, 영문 구역 라벨, 몸짓의 DJ 용어, 큰 숫자."
  wordmark:   { family: Unbounded, size: 22px, weight: 600, letterSpacing: -0.02em }
  hero:       { size: "clamp(40px, 6.4vw, 80px)", weight: 580, lineHeight: 1.08, letterSpacing: -0.045em }
  statement:  { size: "clamp(28px, 4vw, 52px)", weight: 520, lineHeight: 1.22, letterSpacing: -0.035em }
  section:    { size: "clamp(28px, 3.4vw, 44px)", weight: 580, lineHeight: 1.15, letterSpacing: -0.035em }
  card-title: { size: 26px, weight: 620, lineHeight: 1.2, letterSpacing: -0.03em }
  lead:       { size: "clamp(17px, 1.6vw, 20px)", weight: 420, lineHeight: 1.55, letterSpacing: -0.01em }
  body:       { size: 16px, weight: 420, lineHeight: 1.6, letterSpacing: -0.005em }
  label:      { family: Unbounded, size: 13px, weight: 500, letterSpacing: 0.02em }
  caption:    { size: 13px, weight: 500, lineHeight: 1.4, letterSpacing: 0 }
  button:     { size: 16px, weight: 600, lineHeight: 1 }

rounded:
  sm: 8px
  md: 12px
  card: 24px
  block: 32px
  pill: 999px

spacing:
  unit: 8px
  page-pad: 48px
  page-pad-mobile: 16px
  max-width: 1200px
  section: 120px
  section-mobile: 80px
  block-pad: 64px
  block-pad-mobile: 28px
  card-pad: 28px
  card-gap: 16px

motion:
  ease: cubic-bezier(.2,.7,.1,1)
  reveal: "translateY 16px, 0.9s, 투명도는 바꾸지 않음"
  press: "scale .97, 0.15s"
  reduced-motion: 모든 전환과 애니메이션을 끈다
---

# KKAL 랜딩 디자인 가이드 v0.1

B안(창업 디벨롭) 랜딩 페이지에 쓰는 디자인 시스템입니다. Clay의 색 카드 문법과 Figma의 색 블록 구역 나누기를 합치고, cize의 포트폴리오 가이드 v0.3에 적힌 금지 사항을 그대로 따릅니다. 이 문서의 내용은 모듈 다섯 색을 빼면 모두 **제안** 상태입니다(15. 확정 항목과 제안 항목).

## 1. 개요

| 구역 | 역할 | 표현 |
| --- | --- | --- |
| 첫 화면 | 무엇을 하는 제품인지 한 문장으로 알립니다. | 흰 바탕 7:5 분할. 왼쪽에 제목과 알림 신청, 오른쪽에 바디 모듈과 잔 모듈 그림 칸 |
| 문제 | 왜 필요한지 한 문장으로 말합니다. | 큰 글자 문장 하나 |
| 쓰는 방법 | 세 단계를 차례로 설명합니다. | 숲 색 블록(Figma식) 위에 단계 셋 |
| 몸짓 | 다섯 몸짓을 소리로 들려줍니다. | 흰 바탕 위 연한 면 카드 다섯 장과 소리 데모 |
| 잔 모듈 | 다섯 잔을 소개합니다. | 모듈 색 카드 다섯 장(Clay식) |
| 혼자와 함께 | 혼자 쓸 때와 함께 쓸 때를 비교합니다. | 먹색 블록, 두 칸 |
| 구성 | 기본 세트와 추가 잔을 소개합니다. | 흰 바탕 카드 두 장 |
| 알림 신청 | 전환 지점입니다. | 들 색 블록과 메일 입력 |

## 2. 원본 가이드 대비 변경 사항

| 항목 | 원본 | 변경 | 이유 |
| --- | --- | --- | --- |
| 바탕 | Clay 크림 #fffaf0 | 차가운 흰색 #FBFBFB | 난색 미색 금지(cize 포트폴리오 가이드). 들(#F7F2C5)이 크림 바탕에 묻히는 문제도 함께 없앱니다. |
| 글자색 | Clay #0a0a0a, Figma #000000 | 초록빛 먹색 #1D2624 | 생블랙 금지. 숲 색과 같은 색 계열로 맞춥니다. |
| 색 카드 | Clay 6색(핑크, 틸, 라벤더, 피치, 오커, 크림) | 잔 모듈 5색 | 브랜드 색을 제품 색과 일치시킵니다. Clay 규칙대로 일곱 번째 색은 더하지 않습니다. |
| 색의 의미 | Clay는 기능별로 색을 고름 | 모듈 색은 그 모듈을 가리킬 때만 씀 | 몸짓 카드에 모듈 색을 칠하면 몸짓과 모듈이 짝인 것처럼 읽힙니다. 정보 구조를 위해 색에 한 가지 의미만 줍니다(Webflow의 카테고리 색 규칙). |
| 구역 나누기 | Clay는 카드만 반복 | Figma식 색 블록과 흰 바탕을 번갈아 둠 | 한 화면에 색 블록을 둘 이상 겹쳐 보이지 않게 해서 구역의 경계가 분명해집니다. |
| 버튼 | Clay 12px 모서리, Figma 알약 | 알약 | cize 포트폴리오와 Figma 규칙. 버튼, 칩, 입력창을 알약으로 통일합니다. |
| 제목 글꼴 | Plain Black(라이선스), figmaSans | 한글 Pretendard 580, 영문 Unbounded | 한글 페이지입니다. Clay 원칙(제목 굵기를 과하게 올리지 않음)은 지킵니다. |
| 라벨 | figmaMono 대문자 | Unbounded 500 영문 라벨 | 고정폭 대문자 라벨은 생성형 화면에서 흔한 모양이라 쓰지 않습니다. |
| 일러스트 | Clay 3D 클레이 렌더 | 시안에서는 평면 SVG, 이후 실물 렌더로 교체 | 실물 모듈 렌더가 아직 없습니다. 렌더가 준비되면 같은 그림 칸에 넣습니다. |
| 그림자, 그라데이션 | Figma는 떠 있는 타일에 약한 그림자 | 쓰지 않음 | cize 금지 사항. 깊이는 색 면 대비로만 냅니다. |

## 3. 색상

**금지**: 난색 미색(베이지, 아이보리, 크림), 생화이트, 생블랙, 장식용 그라데이션, 보라색 계열 UI 색.

### 바탕과 글자
- **Canvas** `#FBFBFB`: 페이지 바탕.
- **Surface Soft** `#F0F2F1`: 몸짓 카드, 그림 칸, 입력창 바탕. 바탕보다 한 단계 짙은 회녹색입니다.
- **Ink** `#1D2624`: 제목, 본문, 버튼, 먹색 블록. Canvas 위 대비 15.0:1.
- **Muted** `#57625F`: 캡션과 보조 정보에만 씁니다. Canvas 위 6.1:1, Surface Soft 위 5.6:1. 본문에는 쓰지 않습니다.
- **On Dark** `#FBFBFB`: 숲, 밤, 먹색 블록 위의 글자.

### 잔 모듈 색
| 모듈 | 값 | 카드 글자 | 글자 대비 | 비고 |
| --- | --- | --- | --- | --- |
| 숲 | `#265F56` | On Dark | 7.1:1 | 쓰는 방법 블록의 바탕으로도 씁니다. |
| 밤 | `#6F3C66` | On Dark | 8.1:1 | 모듈 카드에만 씁니다(보라색 UI 금지와 구분). |
| 노을 | `#F15B5C` | Ink | 4.7:1 | 흰 글자는 3.2:1이라 쓰지 않습니다. |
| 여울 | `#9ED7E0` | Ink | 9.8:1 |  |
| 들 | `#F7F2C5` | Ink | 13.6:1 | Canvas와 대비가 1.1:1이라 카드에 안쪽 테두리(`hairline`)를 둡니다. 알림 신청 블록의 바탕으로도 씁니다. |

### 규칙
- 모듈 색은 모듈 카드, 모듈 그림, 그리고 숲(쓰는 방법)과 들(알림 신청) 두 블록에만 씁니다.
- 버튼, 링크, 선택 상태는 먹색입니다. 모듈 색으로 버튼을 칠하지 않습니다.
- 색 카드는 같은 색이 두 번 이어지지 않게 숲, 밤, 노을, 여울, 들 순서로 둡니다.

## 4. 타이포그래피

- **Pretendard Variable**: 한글 제목과 본문. 제목은 580, 본문은 420입니다. 굵기를 700 이상으로 올리지 않습니다.
- **Unbounded**: 워드마크 KKAL, 영문 구역 라벨(How, Gestures, Modules, Set), 몸짓 카드의 DJ 용어(Remix, Tune, Beat, Loop, Save). 한 줄 안에서 한글과 섞지 않습니다.
- 대체 글꼴: `-apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif`.
- 모든 텍스트에 `word-break: keep-all`, 줄글에 `text-wrap: pretty`, 요약 문단에 `max-width: 34em; text-wrap: balance`를 적용합니다(WRITING_RULES W-TYP-09).
- 자간은 글자가 클수록 좁힙니다. 16px 이하는 거의 0으로 둡니다.

## 5. 레이아웃

- 상단 메뉴: KKAL 워드마크, How, Gestures, Modules, Set, 알림 신청 버튼. 메뉴 이름은 영어입니다(WRITING_RULES CONFIG).
- 최대 폭 1200px, 좌우 여백 48px(모바일 16px), 구역 사이 120px(모바일 80px).
- 색 블록은 콘텐츠 폭 전체를 차지하고 모서리 32px, 안쪽 여백 64px(모바일 28px)입니다. 768px 이하에서는 화면 끝까지 붙이고 모서리를 없앱니다(Figma 규칙).
- 구분선을 줄마다 긋지 않습니다. 구역은 여백과 색 면으로만 나눕니다. 선은 들 카드의 안쪽 테두리와 입력창 테두리 두 곳에만 씁니다.
- 번호(01, 02, 03)는 실제로 순서가 있는 쓰는 방법 세 단계에만 씁니다.

## 6. 깊이

| 단계 | 처리 | 쓰는 곳 |
| --- | --- | --- |
| 평면 | 그림자와 선 없음 | 모든 구역, 상단 메뉴 |
| 연한 면 | Surface Soft 채움 | 몸짓 카드, 그림 칸 |
| 색 면 | 모듈 색 채움 | 모듈 카드, 색 블록 |

그림자는 쓰지 않습니다. 앞뒤 관계는 바탕과 면의 명도 차이로만 만듭니다.

## 7. 모양

| 토큰 | 값 | 쓰는 곳 |
| --- | --- | --- |
| `sm` | 8px | 작은 칩 안쪽 요소 |
| `md` | 12px | 그림 칸 안의 작은 그림 |
| `card` | 24px | 몸짓 카드, 모듈 카드, 구성 카드, 그림 칸 |
| `block` | 32px | 색 블록 |
| `pill` | 999px | 버튼, 입력창, 라벨 칩 |

## 8. 컴포넌트

- **버튼(주)**: 먹색 알약, On Dark 글자, 높이 52px, 좌우 26px.
- **버튼(보조)**: Surface Soft 알약, 먹색 글자. 색 블록 위에서는 Canvas 알약.
- **몸짓 카드**: Surface Soft, 모서리 24px, 안쪽 28px. 위에서부터 영문 DJ 용어 라벨, 한글 몸짓 이름, 한 문장 설명, 소리 버튼(재생 아이콘과 "들어 보기"). 재생 중에는 카드 바탕이 먹색으로 바뀌고 글자가 On Dark로 바뀝니다.
- **모듈 카드**: 모듈 색 채움, 모서리 24px. 위쪽에 잔 그림, 아래쪽에 모듈 이름과 소리 성격 한 줄.
- **단계(쓰는 방법)**: 숲 블록 위에 큰 숫자(Unbounded), 두 단어 이상의 단계 제목, 한 문장 설명.
- **알림 신청**: 들 블록 위에 제목, 메일 입력 알약, 먹색 버튼. 제출하면 같은 자리에 완료 문장이 나타납니다.

## 9. 움직임과 소리

- 구역은 아래 16px에서 0.9초 동안 올라옵니다. 투명도는 바꾸지 않아서 움직임이 멈춰 있어도 내용이 보입니다.
- 버튼은 누를 때 0.15초 동안 살짝 작아집니다.
- 몸짓 데모 소리는 Web Audio로 합성합니다. 소리는 사용자가 버튼을 눌렀을 때만 납니다.
- 사용자가 움직임 줄이기를 켜면 모든 전환을 끕니다.

## 10. 할 것과 하지 말 것

### 할 것
- 모듈 색 위 글자는 3장 표의 값을 따릅니다.
- 한 화면에 색 블록은 하나만 보이게 하고, 색 블록 사이에는 흰 바탕을 둡니다.
- 몸짓과 모듈은 색으로 묶지 않습니다.

### 하지 말 것
- 색과 악기를 짝지은 설명을 앞세우지 않습니다(Muse, DropMix 선례와 겹칩니다).
- 술자리, 술상, 주점 같은 말을 쓰지 않습니다. 술자리는 몸짓의 출처로만 발표에서 설명합니다.
- 그림자, 그라데이션, 이모지, 고정폭 대문자 라벨, 회색 본문을 쓰지 않습니다.
- 가격, 출시일, 사양 수치처럼 정해지지 않은 정보를 넣지 않습니다.

## 11. 반응형

| 이름 | 폭 | 바뀌는 점 |
| --- | --- | --- |
| 데스크톱 | 1024px 이상 | 첫 화면 7:5, 몸짓 카드 3열, 모듈 카드 5열 |
| 태블릿 | 768–1023px | 첫 화면 한 열, 몸짓 2열, 모듈 3열 |
| 모바일 | 767px 이하 | 메뉴 링크 숨김(워드마크와 알림 신청만), 몸짓 1열, 모듈 2열, 색 블록 화면 끝까지 |

- 버튼과 입력창 높이는 44px 이상입니다. 어느 폭에서도 가로 스크롤이 생기지 않아야 합니다.

## 12. 문구 규칙

`guidelines/WRITING_RULES.md`를 따르고, 랜딩에서는 아래를 더합니다.

- 문장은 합쇼체 "~합니다"로 씁니다. 라벨과 목록은 명사로 끝내도 됩니다.
- 화면 사용법을 설명하는 안내 문장을 쓰지 않습니다. 버튼 이름만 씁니다(W-UI-01).
- 단계 제목은 두 단어 이상으로 씁니다(W-VOI-03).
- 확정된 사실만 씁니다. 가격, 출시일, 연동 앱, 배터리 같은 사양은 정해지면 넣습니다.
- 공개 전에 `lint.py`(WRITING_RULES 정규식 검사)로 error 0을 확인합니다.

## 13. 쓰는 말

| 쓰는 말 | 쓰지 않는 말 |
| --- | --- |
| 바디 모듈, 잔 모듈 | 술상, 본체, 컵 |
| 짠, 쌓기, 두드리기, 돌리기, 털기 | 건배, 노킹, 스피닝, 셰이킹(영문은 DJ 용어 라벨로만) |
| 섞다, 바꾸다, 튜닝 | WRITING_RULES W-LEX의 홍보 문구 |

## 14. 소스와 도구

- 글꼴: Pretendard Variable(jsDelivr `pretendard@1.3.9`), Unbounded(Google Fonts).
- 소리: Web Audio API(라이브러리 없음). 실제 음원을 쓰게 되면 Tone.js로 바꿉니다.
- 검수: Playwright 스크린샷(390px, 1440px), `lint.py`.

## 15. 확정 항목과 제안 항목

**확정**
- 모듈 다섯 색 값(프로젝트 기존 값).
- cize 금지 사항: 난색 미색, 생화이트·생블랙, 그림자, 그라데이션, 이모지, 회색 본문.

**제안(cize 확인 대기)**
- Clay와 Figma를 섞은 구조, 먹색 #1D2624, Surface Soft #F0F2F1.
- Unbounded를 워드마크와 영문 라벨에 쓰는 안.
- 랜딩 구역 구성(1. 개요의 표)과 모든 카피.
- 몸짓 데모 소리(합성음 시안). 실제 음원으로 바꿀지 결정이 필요합니다.
