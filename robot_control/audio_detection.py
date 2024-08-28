# audio_detection.py
import speech_recognition as sr




def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Args:
        recognizer (sr.Recognizer): The recognizer instance.
        microphone (sr.Microphone): The microphone instance.

    Returns:
        dict: A dictionary with the keys:
            "success" (bool): Whether or not the API request was successful.
            "error" (str | None): None if no error occurred, otherwise a string containing an error message.
            "transcription" (str | None): None if speech could not be transcribed, otherwise the transcribed text.
    """
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio, language="ko-KR")
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def main():
    """Main function to activate Bixby on specific wake word."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please wait a moment. Adjusting for ambient noise...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
    print("Ready for activation word. Say 'Bixby' or equivalent Korean word to activate.")

    while True:
        print("Listening...")
        response = recognize_speech_from_mic(recognizer, microphone)

        if response["transcription"] and "빅스비" in response["transcription"].lower():
            print("Bixby activated! How can I help you?")
            break

        if response["error"]:
            print("ERROR: {}".format(response["error"]))

if __name__ == "__main__":
    main()