# main.py
from robot_control import recognize_speech_from_mic, text_to_tts
import speech_recognition as sr


MODEL_NAME: str = "시리"


def main():
    """Main function to activate voice model on specific wake word."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    text_to_tts("잠시만 기다려 주세요. 주변 소음에 적응하는 중입니다.")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
    
    text_to_tts(f"모델 이름을 불러 명령할 수 있습니다. {MODEL_NAME}을 말해주세요.")

    while True:
        print("Listening...")
        response = recognize_speech_from_mic(recognizer, microphone)

        if response["transcription"] and MODEL_NAME in response["transcription"].lower():
            text_to_tts("로봇이 활성화되었습니다. 명령을 주십시오.")
            response = recognize_speech_from_mic(recognizer, microphone)
            print(response)
            break

        if response["error"]:
            print("ERROR: {}".format(response["error"]))




if __name__=="__main__":
    main()