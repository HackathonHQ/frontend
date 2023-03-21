from tokenize import String
from unicodedata import name
import speech_recognition as sr
import pyttsx3 #pip install pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
name = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def begin():
    speak('Connecting to Mainframe...')

def identify():
    speak('I am AFOGAA, your personal voice assisstant. May i have your name please?')
    global name
    name = takeCommand().lower()

def wishMe():
    global name
    speak("Hello "+str(name)+" and welcome!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



begin()
identify()
wishMe()

if __name__ == "__main__":
    while True:
        inp = takeCommand().lower()
        if 'google' in inp:
            webbrowser.open('')
