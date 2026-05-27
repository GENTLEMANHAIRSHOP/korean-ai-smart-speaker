# Korean AI Smart Speaker 🔊🤖

Raspberry Pi와 Gemini API를 활용해 한국어 음성 대화가 가능한 AI 스마트 스피커를 만드는 프로젝트입니다.

사용자가 "하이 문규"라는 호출어를 말하면 시스템이 음성을 인식하고, 질문을 텍스트로 변환한 뒤 Gemini API 응답을 받아 한국어 음성으로 출력하는 것을 목표로 합니다.

## 프로젝트 소개

이 프로젝트는 라즈베리파이 기반의 한국어 AI 스마트 스피커입니다.

음성 인식, AI 응답 생성, 음성 출력, LCD 표정 표시를 하나로 연결하여 실제 대화형 장치처럼 작동하도록 설계했습니다.

초기 버전은 실제 마이크와 스피커 없이도 PC에서 키보드 입력과 텍스트 출력으로 동작 흐름을 테스트할 수 있습니다.

## 제작 목적

- Raspberry Pi를 활용한 AI 음성 비서 제작
- 한국어 음성 인식과 음성 합성 실험
- Gemini API를 활용한 자연어 대화 구현
- LCD 화면을 통한 표정 출력 기능 구상
- 하드웨어와 AI 서비스를 결합한 스마트 장치 제작

## 주요 기능

- 호출어 "하이 문규" 감지
- 키보드 입력 기반 초기 테스트
- Gemini API 기반 AI 응답 생성
- 한국어 음성 출력 확장 가능
- LCD 표정 표시 확장 가능
- Raspberry Pi 기반 독립 실행 가능

## 사용 기술

- Python
- Raspberry Pi
- Gemini API
- Speech Recognition
- Text-to-Speech
- LCD Display

## 시스템 구조

```txt
User Voice or Keyboard Input
    ↓
Hotword Detection
    ↓
Question Input
    ↓
Gemini API
    ↓
AI Response
    ↓
Text-to-Speech or Text Output
    ↓
LCD Face Expression
```

## 프로젝트 구조

```txt
korean-ai-smart-speaker/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
├── docs/
│   └── system-architecture.md
└── images/
    └── demo-image-here.txt
```

## 실행 방법

### 1. 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 2. Gemini API 키 설정

PowerShell에서는 다음과 같이 임시 환경변수를 설정합니다.

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

### 3. 실행

```bash
python src/main.py
```

## 사용 예시

```txt
Korean AI Smart Speaker 시작
호출어: 하이 문규
사용 AI: Gemini API
종료하려면 exit 입력

사용자 입력: 하이 문규
호출어 감지됨!
질문을 입력하세요: 오늘 기분 어때?
AI 응답: ...
```

## 향후 개선 계획

- 실제 마이크 입력 연결
- 한국어 음성 인식 적용
- TTS 음성 출력 적용
- LCD 또는 OLED 표정 출력
- Raspberry Pi 자동 실행 설정
- 웨이크워드 감지 정확도 개선
