import os
import time

"""
Korean AI Smart Speaker

초기 테스트용 코드입니다.
실제 마이크, 스피커, LCD를 연결하기 전
스마트 스피커의 기본 흐름을 확인합니다.
"""

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HOTWORD = "하이 문규"


def detect_hotword(user_input: str) -> bool:
    """
    호출어 '하이 문규'가 포함되어 있는지 확인합니다.
    """
    return HOTWORD in user_input


def listen_to_user() -> str:
    """
    초기 버전에서는 실제 음성 인식 대신 키보드 입력을 사용합니다.
    """
    return input("사용자 입력: ")


def generate_ai_response(question: str) -> str:
    """
    AI 응답 생성 부분입니다.
    현재는 테스트용 응답을 반환합니다.
    """
    if not OPENAI_API_KEY:
        return "OPENAI_API_KEY가 설정되지 않았습니다. 현재는 테스트 응답입니다."

    return f"'{question}'에 대한 AI 응답을 생성하는 부분입니다."


def speak_response(response: str):
    """
    음성 출력 함수입니다.
    현재는 print로 출력하고, 나중에 TTS로 교체할 수 있습니다.
    """
    print("AI 응답:", response)


def show_face_expression(expression: str):
    """
    LCD 표정 출력 함수입니다.
    현재는 텍스트 표정으로 테스트합니다.
    """
    expressions = {
        "idle": "( -_- )",
        "listening": "( ・_・)",
        "thinking": "( ..?)",
        "speaking": "( ^_^ )",
        "error": "( x_x )"
    }

    print("LCD Face:", expressions.get(expression, "( -_- )"))


def main():
    print("Korean AI Smart Speaker 시작")
    print(f"호출어: {HOTWORD}")
    print("종료하려면 exit 입력")

    show_face_expression("idle")

    while True:
        user_input = listen_to_user()

        if user_input.lower() == "exit":
            print("프로그램을 종료합니다.")
            break

        if detect_hotword(user_input):
            show_face_expression("listening")
            print("호출어 감지됨!")

            question = input("질문을 입력하세요: ")

            show_face_expression("thinking")
            time.sleep(1)

            response = generate_ai_response(question)

            show_face_expression("speaking")
            speak_response(response)

            show_face_expression("idle")
        else:
            print("호출어가 감지되지 않았습니다.")


if __name__ == "__main__":
    main()
