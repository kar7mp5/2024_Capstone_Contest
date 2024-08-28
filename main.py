# main.py
from robot_control import recognize_speech_from_mic
import speech_recognition as sr


MODEL_NAME: str = "시리"


def main():
    """Main function to activate Bixby on specific wake word."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please wait a moment. Adjusting for ambient noise...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
    print(f"Ready for activation word. Say '{MODEL_NAME}' or equivalent Korean word to activate.")

    while True:
        print("Listening...")
        response = recognize_speech_from_mic(recognizer, microphone)

        if response["transcription"] and MODEL_NAME in response["transcription"].lower():
            print("Bixby activated! How can I help you?")
            response = recognize_speech_from_mic(recognizer, microphone)
            print(response)
            break

        if response["error"]:
            print("ERROR: {}".format(response["error"]))




if __name__=="__main__":
    main()