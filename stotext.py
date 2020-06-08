import speech_recognition as sr
def record():
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        return text

record()
