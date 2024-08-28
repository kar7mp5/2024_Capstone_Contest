# tts.py
from gtts import gTTS
from playsound import playsound
import os




def text_to_tts(itext, language='ko'):
    """text to tts
    Convert text to audio file and play the audio file.
    
    Args:
        text (str): converted text.
        language (str): language selection; 'ko' and 'en'.
           
    Returns:
        Audio file: .mp3 format audio file.
                    This file would be removed.
    """
    # setup the file path.
    _path = os.path.join(os.getcwd(), "tts.mp3")
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    audio_file = gTTS(text=itext, 
                 lang=language,
                 slow=False)

    # Saving the converted audio in a mp3 file named
    audio_file.save(_path)

    # Playing the converted file without opening a new window
    playsound(_path)
    
    # Delete unusal audio file.
    os.remove(_path)


    

if __name__=="__main__":
    text_to_tts("안녕하세요? 저는 김민섭입니다.")