# WRITING_RULES v1.1

AI가 쓴 티가 나지 않는 한국어 문구를 쓰기 위한 규칙입니다. 포트폴리오, 소개 페이지, 프로젝트 설명, UI 문구에 씁니다.

- 근거: 포트폴리오 웹사이트 제작(2026-11-12 ~ 11-16) 중 사용자가 직접 지적한 문장과 최종 승인된 문구. 예시의 작품명과 회사명은 설명을 위한 것이며, 다른 프로젝트에 붙여 넣을 때는 그대로 두어도 됩니다.
- 자동 검사: `lint_writing.py`가 이 문서에서 `detect.regex`가 있는 규칙을 실행합니다. 최종 사이트 문구(data.js, index.html)를 검사하였을 때 error 0건이었고, warn 7건은 모두 작품 안의 게임 문구와 이미지 캡션처럼 의도한 표현이었습니다.
- 우선순위: 사용자가 그 자리에서 한 지시 > 사용자가 직접 쓴 문장 > 이 문서 > 일반적인 글쓰기 관습.

```text
# 다른 프로젝트에서 쓰는 법
1. 이 파일과 lint_writing.py를 프로젝트에 복사합니다.
2. CLAUDE.md나 지시문에 아래 한 줄을 넣습니다.
   "문구를 쓰거나 고칠 때 WRITING_RULES.md를 따르고, 제출 전에 lint_writing.py로 검사해 error를 0으로 만든다."
3. 프로젝트마다 바뀌는 값은 0장의 CONFIG만 고칩니다.
```

---

## 0. CONFIG (프로젝트마다 정하는 값)

```yaml
voice:
  style: 합쇼체            # 한 매체 안에서 하나만 쓴다. lint는 파일 안의 다수 문체를 기준으로 섞임을 잡는다.
  past_work: "~하였습니다"  # 이미 끝낸 작업. 학생 보고서 투. (예시 프로젝트의 결정)
  present: "~합니다"        # 지금 하는 일, 습관, 취향.
  list_item: 명사형 허용     # 목록 항목과 라벨은 명사로 끝내도 된다.
labels:
  menu_lang: en            # 한국어로 쓰면 번역체가 되는 짧은 라벨은 영어로 쓴다. (Work, About, Contact)
terms:                     # 사용자가 정한 용어. 사용자가 고친 말은 다시 바꾸지 않는다.
  - { avoid: "캐릭터 IP",   use: "캐릭터, 캐릭터 디자인" }
  - { avoid: "팀 (실무)",   use: "직무" }
  - { avoid: "근거 작업",   use: "관련 작업" }
  - { avoid: "작업 메모",   use: "작업 방식" }
  - { avoid: "협업 (반복)", use: "핵심 활동, 산학 프로젝트" }
limits:
  sentence_chars_warn: 100
  clause_commas_per_sentence: 2
  same_word_per_paragraph: 3
  summary_sentences: 2-3
```

---

## 1. 원칙

다섯 가지 원칙이 모든 규칙의 근거입니다. 규칙에 없는 상황에서는 이 원칙으로 판단합니다.

| ID | 원칙 | 판정 질문 |
| --- | --- | --- |
| P1 | 사실, 행동, 결과 순서로 씁니다. | 이 문장을 읽고 어떤 툴에서 무슨 행동을 했는지 알 수 있는가? |
| P2 | 다른 작업에 그대로 붙여 쓸 수 있는 문장은 버립니다. | 프로젝트명만 바꾸면 다른 작업에도 맞는 문장인가? 그렇다면 다시 씁니다. |
| P3 | 증명할 수 있는 만큼만 주장합니다. | 스크린샷 한 장, 수상 기록, 공개 매체로 증명할 수 있는가? |
| P4 | 설명이 필요한 화면은 문장이 아니라 화면을 고칩니다. | 이 안내 문장을 지워도 사용자가 화면을 이해하는가? |
| P5 | 사용자가 쓴 문장과 용어를 지킵니다. | 사용자 원문의 사실과 말투를 바꾸었는가? |

---

## 2. 규칙

형식은 아래와 같습니다. `severity`가 `error`이면 제출 전에 반드시 고치고, `warn`이면 문맥을 보고 판단하고, `manual`은 사람이 읽어서 확인합니다.

```yaml
id:        규칙 ID (lint 출력과 같음)
severity:  error | warn | info | manual
detect:    regex 또는 판정 방법
fix:       고치는 방향
bad/good:  나쁜 예와 좋은 예 (실제 사례는 [실제] 표시)
```

### 2.1 LEX: 어휘

```yaml
- id: W-LEX-01
  name: 추상어로 무게 만들기
  severity: error
  detect: { regex: '시너지|경험을 (?:선사|제공)|가치를 전달|서사적|차별화된|혁신적인?|유기적(?:으로|인)|새로운 차원|몰입감|한계를 뛰어넘' }
  why: 사용자가 가장 싫어한 표현 묶음이다. 어느 작업에나 붙일 수 있어서 P2를 어긴다.
  fix: 무엇을, 어떤 툴로, 어떻게 했는지로 바꾼다.
  bad:  다양한 기술을 유기적으로 결합하여 풍부한 비주얼 경험을 제공하였습니다.
  good: Midjourney로 장면 이미지를 생성하고 Photoshop에서 조명과 합성 오류를 수정하였습니다.   # [실제] 인수인계 문체 가이드

- id: W-LEX-06
  name: 대상 없는 추상어
  severity: warn
  detect: { regex: '흐름|리듬감?|결합(?:하여|해|한|된)|확장(?:성|하|해|된)|여정|감성적인?|분위기를 자아' }
  allow: 구체적인 대상과 함께 쓴 경우. "작업 흐름", "AI 활용 흐름"은 허용한다.
  bad:  영상 전반의 감성적인 흐름과 리듬감을 고려하였습니다.
  good: 컷 길이와 음악 시작점을 조정해 주요 장면이 강조되도록 편집하였습니다.

- id: W-LEX-02
  name: 자기 평가 형용사
  severity: warn
  detect: { regex: '완벽한|최고의|탁월한|독보적인?|압도적인?|놀라운|특별한|매력적인|인상적인|세련된|다채로운|풍부한|뛰어난' }
  fix: 형용사를 지우고 결과로 증명한다. 수상명, 공개 매체, 기간, 수치를 쓴다.
  bad:  프로젝트의 높은 완성도와 차별화된 성과를 달성하였습니다.
  good: 완성한 영상은 본부관 스크린과 학교 홈페이지에서 약 한 달 동안 공개되었습니다.   # [실제] 최종 사이트

- id: W-LEX-03
  name: 강조 부사
  severity: warn
  detect: { regex: '(?:^|\s)(?:정말|매우|굉장히|진정한|그야말로|비로소|무엇보다)(?=\s)' }
  fix: 지우고 읽어 본다. 뜻이 같으면 지운다.

- id: W-LEX-04
  name: 비유 동사
  severity: warn
  detect: { regex: '담아 ?냈|녹여 ?냈|풀어 ?냈|빚어 ?냈|그려 ?냈|엮어 ?냈|숨을 불어넣|생명력을 불어넣|옷을 입혔' }
  fix: 일반 동사로 바꾼다. 제작하였습니다, 적용하였습니다, 표현하였습니다, 설계하였습니다.
  bad:  캐릭터에 생명력을 불어넣었습니다.
  good: 멤버별 얼굴을 유지한 캐릭터 에셋을 생성하고 광고 콘셉트에 맞춰 스타일링하였습니다.   # [실제]

- id: W-LEX-05
  name: 업계 유행어
  severity: warn
  detect: { regex: '인사이트|임팩트|솔루션|레버리지|아이덴티티를 구축|브랜드 경험|사용자 경험을|퀄리티 높은|하이엔드' }
  fix: 한국어 일반 어휘나 구체적 결과로 바꾼다.

- id: W-LEX-07
  name: 같은 말 반복으로 생기는 과시
  severity: manual
  detect: 한 화면에서 같은 자랑성 단어(협업, 리드, 주도 등)가 세 번 이상 보이는지 읽는다.
  why: "협업 협업 하면 건방져 보임" [실제 지적]
  fix: 한 번만 남기고, 분류 이름은 중립적인 말로 바꾼다. (협업 → 핵심 활동, 산학 프로젝트)

- id: W-LEX-08
  name: 사용자 용어 바꾸기
  severity: manual
  detect: CONFIG.terms의 avoid 목록과 사용자가 고친 이력을 대조한다.
  why: 사용자가 "캐릭터 IP"를 금지하였고, 소속이 아닌 팀을 "팀"으로 적은 것을 "직무"로 고쳤다. [실제]
  fix: 사용자가 정한 말만 쓴다. 더 그럴듯한 말로 바꾸지 않는다.
```

### 2.2 STR: 문장 구조

AI 문장은 어휘보다 구조에서 먼저 티가 납니다. 특히 무언가를 부정하고 나서 진짜를 말하는 대비 구조를 금지합니다.

```yaml
- id: W-STR-01
  name: 부정 대비
  severity: error
  detect: { regex: '(?:단순히|그저|단지)[^.]{0,30}(?:이|가)? 아니(?:라|고)|[가-힣]+(?:을|를) 넘어(?:서)?\s|뿐만 아니라|뿐 아니라' }
  fix: 부정하는 쪽(A)을 지우고 B만 사실로 쓴다.
  bad:  기존의 관습을 넘어 새로운 콘텐츠 경험을 제안하였습니다.
  good: 고양이 캐릭터가 캠퍼스를 소개하는 브이로그 형식으로 학사 제도를 설명하였습니다.   # [실제] 인수인계 예시

- id: W-STR-02
  name: A가 아니라 B
  severity: warn
  detect: { regex: '[가-힣]+(?:이|가) 아니라 [가-힣]+' }
  allow: 실제 오해를 바로잡는 문장. (예: "실물 카드 게임이며 디지털 화면용 작업이 아닙니다"처럼 읽는 사람이 틀리게 볼 근거가 있을 때)

- id: W-STR-03
  name: A는 두고 B로
  severity: warn
  detect: { regex: '[가-힣]+(?:은|는) 두고' }
  why: v1 피드백에서 해석 문장과 함께 금지되었다. [실제]
  fix: 바꾼 결과만 쓴다.

- id: W-STR-04
  name: 의도만 있고 행동이 없는 문장
  severity: warn
  detect: { regex: '고자 (?:한다|합니다|하였|했)|고자 하는' }
  fix: 실제로 한 일을 쓴다.
  bad:  작업의 완성도를 높이고자 하였습니다.
  good: 프롬프트를 회차별로 정리하여 다음 회차 생성에 다시 사용하였습니다.

- id: W-STR-05
  name: 해석과 의의 부여
  severity: warn
  detect: { regex: '의미(?:가|를) (?:있|갖|가지)|의의가|라는 점에서|(?:을|를) 보여 ?줍니다|(?:을|를) 증명(?:합니다|한다|하였)|시사(?:합니다|한다)|돋보이|빛을 발' }
  allow: 이미지 캡션에서 "~의 구조를 보여 줍니다"처럼 그림이 보여 주는 대상을 문자 그대로 말할 때.
  fix: 판단은 읽는 사람에게 맡긴다. 만든 것과 근거만 쓴다.   # [실제] v1 규칙 "만든 것과 근거만 쓰고 해석 문장은 쓰지 않는다"

- id: W-STR-06
  name: 결론 연결어
  severity: warn
  detect: { regex: '(?:^|[.\s])(?:결과적으로|이를 통해|이처럼|이렇듯|궁극적으로|더 나아가|나아가)(?=[\s,])' }
  fix: 앞 문장을 요약하거나 부풀리는 문장이면 통째로 지운다.

- id: W-STR-07
  name: 표어형 대구
  severity: warn
  detect: { regex: '[가-힣]+(?:을|를) [가-힣]+하고, [가-힣 ]+(?:으로|로|을|를) [가-힣]+합니다\.' }
  why: 같은 길이의 동사 두 개가 짝을 이루는 문장은 슬로건처럼 읽힌다. 소개 첫 문장 "콘텐츠와 비주얼을 기획하고, 다양한 매체로 구현합니다."를 사용자가 AI 같다고 느꼈다. [실제]
  fix: 짝을 깨거나(끝을 "구현하고 있습니다"처럼 바꾸기), 한쪽을 구체적인 사실로 바꾼다. 소개 첫 문장은 사용자에게 후보를 보여 주고 고르게 한다.

- id: W-STR-08
  name: 질문형 훅과 감탄
  severity: info
  detect: { regex: '[가-힣][?!]$' }
  allow: 작품명("gecko? gecko!")과 작품 안의 문구.

- id: W-STR-09
  name: 삼단 나열 수식
  severity: manual
  detect: 형용사나 명사구 세 개를 같은 꼴로 늘어놓아 리듬을 만든 문장을 읽어서 찾는다. ("감각적이고, 따뜻하며, 깊이 있는")
  fix: 하나만 남기고, 남긴 것도 사실로 바꿀 수 있으면 바꾼다.

- id: W-STR-10
  name: 콜론 부제 제목
  severity: manual
  detect: "X: Y의 재해석" 같은 제목.
  allow: 실제 작품명에 콜론이 들어 있을 때. ("茶茶日常 : 오늘의탕")
  fix: 작업명은 사용자가 쓴 이름 그대로 쓴다. 이름이 없는 작업은 "무엇을 만든 작업인지"로 짓는다. ("류이치 사카모토 인터뷰 북과 CD 커버")
```

### 2.3 TRN: 번역체

```yaml
- { id: W-TRN-01, severity: warn,  regex: '(?:을|를) 통해(?:서)?',       fix: "'~로', '~에서', '~하여'" }
- { id: W-TRN-02, severity: error, regex: '에 있어(?:서)?',             fix: "'~에서', '~할 때'" }
- { id: W-TRN-03, severity: warn,  regex: '(?:을|를) 가지(?:고 있|는|다|며)|(?:을|를) 갖는', fix: "'~이 있다', '~하다'" }
- { id: W-TRN-04, severity: error, regex: '되어지|되어진|되어져|되어졌|하여지|하여졌', fix: "'~되었습니다' 또는 능동" }
- { id: W-TRN-05, severity: error, regex: '하는 것이 가능',               fix: "'~할 수 있다'" }
- { id: W-TRN-06, severity: warn,  regex: '에 의해(?:서)?',             fix: 주어를 세워 능동으로 }
- { id: W-TRN-07, severity: warn,  regex: '로부터',                     fix: "'~에서', '~에게서'" }
- { id: W-TRN-08, severity: info,  regex: '(?:^|\s)하나의 ',            fix: "지워도 뜻이 같으면 지운다. 사용자 원문이면 둔다." }
- { id: W-TRN-09, severity: warn,  regex: '그것은|그것을|그들은|그녀',     fix: 명사를 다시 쓰거나 생략 }
- { id: W-TRN-10, severity: warn,  regex: '(?:에 대한|에 대해) [^.]{0,20}(?:에 대한|에 대해)', fix: 하나를 동사로 풀기 }
```

번역체를 피하려다 더 어색해지는 짧은 라벨은 영어로 씁니다. 메뉴는 Work, About, Contact로 썼고, 사용자가 "번역체가 될 바엔 영어도 괜찮다"고 하였습니다. [실제]

### 2.4 VOI: 문체와 어미

```yaml
- id: W-VOI-01
  name: 문체 섞임
  severity: warn
  detect: lint가 파일 안에서 가장 많이 쓴 문체(합쇼체, 해요체, 해라체, 명사형)를 기본으로 정하고, 다른 문체로 끝난 문장을 표시한다. --endings로 직접 지정할 수 있다.
  fix: CONFIG.voice를 따른다. 끝낸 작업은 "~하였습니다", 지금 하는 일은 "~합니다".
  allow: 작품 안에 실린 문구(게임 카드의 "배치하세요" 등)는 원문을 둔다.

- id: W-VOI-02
  name: 줄글을 명사로 끝내기
  severity: manual
  detect: 줄글 문장이 "~제작.", "~진행 중." 처럼 명사로 끝나는지 본다.
  fix: 서술어로 끝맺는다. 목록 항목, 라벨, 캡션은 명사로 끝내도 된다.

- id: W-VOI-03
  name: 한 단어 단계 제목
  severity: manual
  detect: 단계 카드와 구역 제목이 "전시", "기획"처럼 한 단어인지 본다.
  why: 단계 카드에 "전시"처럼 한 단어로 쓰는 라이팅을 사용자가 금지하였다. [실제]
  fix: 무엇을 했는지 두 단어 이상으로 쓴다. (전시 → 조형전 출품, 기획 → 기획안과 스토리보드)

- id: W-VOI-04
  name: 조사 생략
  severity: manual
  detect: 명사만 이어 붙인 문장을 읽어서 찾는다.
  bad:  지출 비용 추론 용도의 토큰 카운트 함수의 오류 상황에서
  good: 지출한 비용을 추론하는 토큰 카운트 함수에 오류가 생기면
```

### 2.5 FACT: 사실과 기여

자동으로 잡을 수 없지만 가장 중요한 묶음입니다. 사실을 하나라도 지어내면 문장 품질과 상관없이 실패입니다.

```yaml
- id: W-FACT-01
  name: 확인한 사실만 쓰기
  severity: manual
  rule: 기여도, 수상, 공개 일정, 기간, 툴 숙련도, 인원수는 사용자가 확인한 값만 쓴다. 빈칸은 추측으로 채우지 않고 그 구역을 뺀다.

- id: W-FACT-02
  name: 기여 범위의 동사
  severity: manual
  rule: 본인이 한 일을 팀 전체가 한 것처럼 쓰지 않는다. 반대로 본인 기여를 "참여"라는 말로 줄이지 않는다. 맡은 일은 항목으로 따로 적는다.
  good: "드라마에서는 1, 2, 3, 5화의 영상 생성과 가편집을 맡았고, 극 중 공간 에셋과 키아트도 제작하였습니다."   # [실제]

- id: W-FACT-03
  name: 상태 어휘 구분
  severity: manual
  rule: 완료, 공개 예정, 진행 중, 수상, 선정, 출품을 섞지 않는다. 수상명은 증빙된 명칭 전체를 쓴다.
  good: "대학부 최종 선정작으로 부총리 겸 기획재정부 장관상을 수상하였습니다."   # [실제]

- id: W-FACT-04
  name: 고유명과 관계 표기
  severity: manual
  rule: 회사, 그룹, 작품 이름은 사용자가 공개를 허락한 것만 쓴다. 관계가 복잡하면 사용자에게 표기 후보를 보여 주고 고르게 한다.
  good: "광고 비딩 AI 시안 외주"   # [실제] "외주 프로덕션" 대신 사용자가 고른 표기

- id: W-FACT-05
  name: 사용자 원문 보존
  severity: manual
  rule: 사용자가 직접 쓴 소개 문장은 사실과 말투를 바꾸지 않는다. 고칠 곳이 보이면 고친 안을 따로 제시한다.

- id: W-FACT-06
  name: 표절 오해 차단
  severity: manual
  rule: 특정 작가의 스타일을 차용한 스터디는 차용 사실과 목적을 한 문장으로 밝힌다.
  good: "Midjourney에서 스타일과 캐릭터의 일관성이 유지되는 조건을 확인하려고 진행한 스터디입니다. 팀 버튼 감독의 스타일을 참고 기준으로 삼았고 …"   # [실제]
```

### 2.6 UI: 화면 문구

```yaml
- id: W-UI-01
  name: 사용 안내 문구
  severity: error
  detect: { regex: '누르면|클릭하(?:면|세요|여)|눌러 ?(?:보|주)세요|스크롤(?:하세요|해 ?보세요|하면)|확인해 ?보세요|살펴보세요|자세히 알아보|아래에서 확인|위에서 보듯' }
  why: "UI만 보고 이해되어야 한다." [실제]
  fix: 문구를 지우고 화면을 고친다. 커서 라벨("자세히 보기")처럼 짧은 동작 이름만 허용한다.

- id: W-UI-02
  name: 공개 불가 설명문
  severity: warn
  detect: { regex: '공개하지 않습니다|공개할 수 없|공개가 어려|비공개로 진행|보안상' }
  bad:  진행 중인 작업이라 결과물을 공개하지 않습니다.   # [실제 지적] "AI 같다"
  good: (상태 라벨) 공개 예정

- id: W-UI-03
  name: 점수와 범례 설명
  severity: error
  detect: { regex: '\d점 (?:기준|만점)|범례|상/중/하|[1-5]점은' }
  fix: 채운 칩과 눈금만으로 숙련도가 읽히게 한다.

- id: W-UI-04
  name: 쓸모없는 메타 표기
  severity: warn
  detect: { regex: '(?:^|\s)\d{2}-\d(?=\s|$)|그림 ?\d+|Fig\. ?\d|\(\d+장\)|\(\d+단계\)|총 \d+(?:개|장|단계)' }
  why: "이런 쓸모없는 요소가 정말 AI스럽게 만드는 요소 중 하나" (제목 옆 단계 수, 이미지 수, 08-1 같은 이미지 번호) [실제]
  fix: 지운다. 캡션은 번호 없이 이미지에 붙인다.

- id: W-UI-05
  name: 섹션 설명
  severity: manual
  rule: 섹션 설명이 필요하면 한 문장으로 끝낸다. ("기타 그래픽 작업과 활동입니다.")
```

### 2.7 TYP: 조판

글자를 화면에 앉히는 규칙입니다. 문장이 좋아도 줄바꿈이 어색하면 기계가 만든 페이지처럼 보입니다.

```yaml
- { id: W-TYP-01, severity: error, regex: '—',                     fix: 쉼표, 콜론, 접속사, 문장 나누기 }
- { id: W-TYP-02, severity: warn,  regex: '(?<![\d.])\s–\s(?![\d])', fix: en dash는 숫자 범위(2026.07 – 2026.08)에만 }
- { id: W-TYP-03, severity: warn,  regex: '…|\.\.\.',               fix: 문장을 끝맺는다 }
- { id: W-TYP-05, severity: warn,  detect: 한 문장에 괄호 2쌍 이상,   fix: 하나만 남기고 본문으로 }
- { id: W-TYP-06, severity: warn,  detect: 한 문장에 중간점(·) 2개 이상, fix: "'와/과', 쉼표" }

- id: W-TYP-07
  name: 한 글자 단어 줄끝 금지
  severity: error (런타임)
  why: "새" 같은 한 글자 단어만 줄 끝에 남는 줄바꿈을 줄글 전체에서 금지하였다. [실제]
  fix: 한 글자 한글 단어와 다음 단어를 줄바꿈 없는 공백으로 묶는다. 아래 tie().

- id: W-TYP-08
  name: 쉼표 뒤 한 단어 줄끝 금지
  severity: error (런타임)
  why: "테스트하고, 회차"처럼 쉼표 뒤 다음 구절의 첫 단어 하나만 줄 끝에 걸리면 어색하다. [실제]
  fix: 구절을 끝내는 쉼표(~고, ~며, ~여 등) 뒤에서 그 단어가 혼자 걸리면 쉼표 뒤에서 줄을 바꾼다. 낱말 나열 쉼표는 두고, 창 크기가 바뀌거나 새 내용이 열릴 때 다시 계산한다. 아래 commaBreak().

- id: W-TYP-09
  name: 줄글 폭과 마지막 줄 길이
  severity: error (런타임)
  why: 팝업 요약 문장이 가로로 너무 길게 이어진 뒤에야 줄을 바꾸어 읽기 어려웠다. 마지막 줄에 몇 단어만 남는 것도 같은 문제다. [실제, KKAL 중간 공유 페이지]
  rule: 줄글 한 줄은 한글 34자 안팎에서 끊는다(요약 문단 34em, 본문 36em). 두 줄 이상인 문단은 마지막 줄 길이가 첫 줄 길이의 30%를 넘어야 한다.
  fix: 줄글에 max-width를 주고 text-wrap: balance를 쓴다. balance를 쓴 문단에는 commaBreak()를 돌리지 않는다(두 처리가 겹치면 첫 줄이 짧아진다). 제출 전에 폭마다 줄 수와 '마지막 줄 ÷ 첫 줄' 비율을 잰다.
  example: "친구와 모듈을 고르는 단계를 없앴습니다. 잔이 닿은 뒤에는 지금 어느 단계인지, 결과에 누구 곡이 얼마나 들어갔는지 표시하였습니다."는 1440px에서 '결과에' 앞쯤에서 줄을 바꾼다. [실제]
```

```css
/* 한글 줄글 기본값 */
:root { word-break: keep-all; overflow-wrap: break-word; }
p, li, dd, small { text-wrap: pretty; }   /* 마지막 줄에 한 단어만 남는 것을 줄인다 */
.summary { max-width: 34em; text-wrap: balance; }   /* W-TYP-09: 요약 문단 */
.desc    { max-width: 36em; text-wrap: balance; }   /* W-TYP-09: 본문 설명 */
```

```js
/* W-TYP-07: 한 글자 한글 단어를 다음 단어와 묶는다 */
const TIE = /(^|[\s ])([가-힣])[ ](?=\S)/g;
function tie(root = document.body) {
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  for (let n; (n = w.nextNode());) {
    if (/^(SCRIPT|STYLE)$/.test(n.parentNode?.nodeName)) continue;
    let t = n.nodeValue, prev;
    if (!/[가-힣] /.test(t)) continue;
    do { prev = t; t = t.replace(TIE, "$1$2 "); } while (t !== prev);
    if (t !== n.nodeValue) n.nodeValue = t;
  }
}

/* W-TYP-08: 구절 쉼표 뒤 첫 단어가 혼자 줄 끝에 걸리면 쉼표 뒤에서 줄을 바꾼다
   (예시 사이트에서 쓰던 코드를 그대로 옮김. 줄바꿈 위치를 실제 렌더링으로 잰다) */
function commaBreak(root = document.body) {
  root.querySelectorAll("br.cb").forEach(b => b.replaceWith(" "));
  root.normalize();
  const r = document.createRange();
  root.querySelectorAll("p, small, dd, li").forEach(el => {
    if (!el.offsetWidth || el.querySelector("p, li")) return;
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [];
    for (let n; (n = w.nextNode());) nodes.push(n);
    nodes.forEach(node => {
      let k = 0;
      while (node && (k = node.nodeValue.indexOf(", ", k)) > -1) {
        const t = node.nodeValue;
        // 낱말 나열 쉼표(리플렛, 패키지)는 두고, 구절이 끝나는 쉼표(~하고, ~하여)에서만
        if (!/(고|며|여|서|면|데|만|해|와|과)$/.test(t.slice(0, k))) { k += 2; continue; }
        r.setStart(node, k); r.setEnd(node, k + 1);
        const c = r.getClientRects()[0];
        if (!c) { k += 2; continue; }
        let j = k + 2, words = 0, wrapped = false;
        while (j < t.length) {
          let s = t.indexOf(" ", j); if (s < 0) s = t.length;
          r.setStart(node, j); r.setEnd(node, s);
          const rs = r.getClientRects();
          if (!rs.length) break;
          if (Math.abs(rs[0].top - c.top) > 2 || rs.length > 1) { wrapped = true; break; }
          words++; j = s + 1;
          if (words > 1) break;
        }
        if (words === 1 && wrapped) {
          const rest = node.splitText(k + 1);
          rest.nodeValue = rest.nodeValue.slice(1);
          const br = document.createElement("br"); br.className = "cb";
          rest.parentNode.insertBefore(br, rest);
          node = rest; k = 0;
        } else k += 2;
      }
    });
  });
}
let cbT;
const cbAll = () => { clearTimeout(cbT); cbT = setTimeout(() => commaBreak(), 80); };
addEventListener("resize", cbAll);
document.fonts ? document.fonts.ready.then(cbAll) : cbAll();   // 웹폰트가 적용된 뒤에 잰다
tie();
// 팝업처럼 나중에 열리는 내용에도 tie(el)와 commaBreak(el)를 다시 부른다
```

### 2.8 DEN: 밀도

```yaml
- { id: W-DEN-01, severity: warn, detect: 문장 100자 초과,              fix: 한 문장에 목적 하나와 행동 하나 }
- { id: W-DEN-02, severity: warn, detect: 한 단락에 같은 단어 4회 이상,    fix: 주제어가 아니면 바꾸거나 지운다 }
- { id: W-DEN-03, severity: warn, detect: 구절 잇는 쉼표 3개 이상,        fix: 문장을 나눈다. 낱말 나열 쉼표는 세지 않는다 }
- { id: W-DEN-04, severity: warn, detect: "'~적인/~적으로' 3회 이상",    fix: 풀어 쓴다 }

- id: W-DEN-05
  name: 분량 채우기 금지
  severity: manual
  rule: 정보가 적은 작업은 짧게 끝낸다. 화면을 채우려고 문장이나 이미지를 늘리지 않는다. 요약은 2~3문장이며 첫 문장에 "무엇을 만들었는지"를 쓴다.
```

---

## 3. 고쳐 쓴 실제 사례

이 프로젝트에서 사용자가 지적하였거나 고쳐 준 문장입니다. 새 문장을 쓰기 전에 이 표의 왼쪽과 닮았는지 먼저 봅니다.

| 규칙 | 전 | 후 | 이유 |
| --- | --- | --- | --- |
| W-UI-02 | 진행 중인 작업이라 결과물을 공개하지 않습니다. | (라벨) 공개 예정 | 설명문은 AI 같다. 라벨만 쓴다. |
| W-UI-01 | 카드를 누르면 … / 5점 기준 / 범례 | (삭제) | UI만 보고 이해되어야 한다. |
| W-UI-04 | 제목 옆 "4단계", "6장", 이미지 번호 "08-1" | (삭제) | 쓸모없는 작은 요소가 AI처럼 보이게 만든다. |
| W-LEX-07 | 협업, 협업, 협업 | 핵심 활동, 산학 프로젝트 | 반복하면 건방져 보인다. |
| W-LEX-08 | 캐릭터 IP | 캐릭터 디자인 | 사용자가 금지한 용어다. |
| W-LEX-08 | 팀: ○○팀 | 직무: ○○ | 그 팀 소속이 아니었다. |
| W-VOI-03 | 단계 제목 "전시" | 조형전 출품 | 한 단어 라벨 금지. |
| W-STR-07 | 캐릭터를 디자인하고, 생성형 AI로 영상을 만듭니다. | 콘텐츠와 비주얼을 기획하고, 다양한 매체로 구현하고 있습니다. | 영상이 중심처럼 읽혔다(사실 왜곡). 이후 대구 구조도 AI 같다는 의견이 있어 끝을 바꾸었다. |
| W-FACT-04 | 외주 프로덕션 | 광고 비딩 AI 시안 외주 | 실제 관계를 회사명 없이 정확하게. |
| W-FACT-05 | (Claude가 늘린 소개 문단) | 사용자가 다시 쓴 두 문장으로 교체 | 사용자 원문 우선. |
| W-STR-05 | (캡션) 서사, 데뷔 드라마 | 데뷔 과정을 담은 드라마 | 사용자가 그 단어를 쓰지 말라고 하였다. |

---

## 4. 제출 전 체크리스트

```text
[ ] python3 lint_writing.py <파일들>  →  error 0
[ ] warn은 한 줄씩 읽고, 허용(allow)에 해당하지 않으면 고쳤다
[ ] P2: 작업명을 바꿔 넣어도 말이 되는 문장이 없다
[ ] P3: 모든 수치, 상, 공개 매체, 기간을 사용자가 확인하였다
[ ] W-FACT-02: 맡은 일이 작업마다 항목으로 적혀 있고, 팀 전체 일과 구분된다
[ ] W-VOI-03: 단계와 구역 제목이 한 단어가 아니다
[ ] W-TYP-07, 08: 360px, 768px, 1440px 화면에서 한 글자 줄끝과 쉼표 뒤 한 단어 줄끝이 없다
[ ] W-TYP-09: 줄글 한 줄이 한글 34자 안팎에서 끊기고, 마지막 줄이 첫 줄의 30%를 넘는다
[ ] 사용자가 쓴 문장을 바꾼 곳이 있으면 바꾼 이유를 알렸다
```

## 5. lint가 잡지 못하는 것

정규식은 표면만 봅니다. 아래 세 가지는 사람이 읽어야 합니다.

1. 문법은 맞지만 사실이 틀린 문장(W-FACT 전체).
2. 금지어 없이 쓴 공허한 문장. 예를 들어 "작업 전반을 꼼꼼하게 관리하였습니다."는 어떤 규칙에도 걸리지 않지만 P1과 P2를 어깁니다.
3. 맥락상 허용되는 표현. 작품 안의 문구, 실제 작품명, 그림을 문자 그대로 설명하는 캡션은 warn이 나와도 둡니다.
