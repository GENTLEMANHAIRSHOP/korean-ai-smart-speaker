# System Architecture

## 전체 구조

이 프로젝트는 음성 입력, 호출어 감지, AI 응답 생성, 음성 출력, LCD 표정 표시를 연결한 Raspberry Pi 기반 AI 스마트 스피커입니다.

```txt
User Voice / Text Input
        ↓
Hotword Detection
        ↓
Speech Recognition
        ↓
AI Response Generation
        ↓
Text-to-Speech
        ↓
Speaker Output
        ↓
LCD Face Expression
