# __init__.py
from os.path import dirname
from sys import path

path.insert(0, dirname(__file__))

from .audio_detection import recognize_speech_from_mic
# from .control import Controller