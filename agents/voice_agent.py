import speech_recognition as sr
from gtts import gTTS

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)

    except Exception:
        return "Sorry, I could not understand your voice."

def text_to_speech(text, filename="response.mp3"):

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        return filename

    except Exception as e:
        return None