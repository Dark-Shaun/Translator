from gtts import gTTS
import playsound
from playsound import playsound


def texttos(text):
    global m
    tts = gTTS(text)
    m='audio.mp3'
    tts.save(m)
    return m
