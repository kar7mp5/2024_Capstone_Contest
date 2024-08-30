# main.py
from robot_control import Controller
from robot_control import recognize_speech_from_mic, gpt_api


import speech_recognition as sr




MODEL_NAME: str = "시리"
SEC: int = 2


def main():
    """Main function to activate voice model on specific wake word."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("Adjusting the environment sound")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
    

    controller = Controller(17, 22, 24, 23)

    while True:
        print("Listening...")
        response = recognize_speech_from_mic(recognizer, microphone)

        # Get the text
        if response["transcription"] and MODEL_NAME in response["transcription"].lower():
            response = recognize_speech_from_mic(recognizer, microphone)
            
            match gpt_api(response):
                case 1:             # front
                    controller.forward()                                        
                    break
                
                case 2:             # back
                    controller.go_back()
                    break
                
                case 3:             # left
                    controller.left_turn()
                    break
                
                case 4:             # right
                    controller.right_turn()
                    break
                
                case 5:             # etc
                    print("Unacceptable output!!")
                    break
            
            print(response)

        # Exit the program
        if response["transcription"] and '종료' in response["transcription"].lower():
            break

        if response["error"]:
            print("ERROR: {}".format(response["error"]))




if __name__=="__main__":
    main()
