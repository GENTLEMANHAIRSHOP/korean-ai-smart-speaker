# Korean AI Smart Speaker 🔊🤖

Raspberry Pi와 ChatGPT API를 활용해 한국어 음성 대화가 가능한 AI 스마트 스피커를 만드는 프로젝트입니다.

사용자가 "블스"라는 호출어를 말하면 시스템이 음성을 인식하고, 질문을 텍스트로 변환한 뒤 AI 응답을 받아 한국어 음성으로 출력하는 것을 목표로 합니다.

## 프로젝트 소개

이 프로젝트는 라즈베리파이 기반의 한국어 AI 스마트 스피커입니다.

음성 인식, AI 응답 생성, 음성 출력, LCD 표정 표시를 하나로 연결하여 실제 대화형 장치처럼 작동하도록 설계했습니다.

## 제작 목적

- Raspberry Pi를 활용한 AI 음성 비서 제작
- 한국어 음성 인식과 음성 합성 실험
- ChatGPT API를 활용한 자연어 대화 구현
- LCD 화면을 통한 표정 출력 기능 구상
- 하드웨어와 AI 서비스를 결합한 스마트 장치 제작

## 주요 기능

- 호출어 "블스" 감지
- 한국어 음성 인식
- AI 응답 생성
- 한국어 음성 출력
- LCD 표정 표시 확장 가능
- Raspberry Pi 기반 독립 실행 가능

## 사용 기술

- Python
- Raspberry Pi
- Speech Recognition
- Text-to-Speech
- ChatGPT API
- LCD Display

## 시스템 구조

```txt
User Voice
    ↓
Hotword Detection
    ↓
Speech Recognition
    ↓
ChatGPT API
    ↓
Text-to-Speech
    ↓
Speaker Output
    ↓
LCD Face Expression
