import pyttsx3
import webbrowser
import speech_recognition as sr
import datetime
import wikipedia

class Assist:
    def __init__(self):
        pass
    
    def speak(self, audio):
        # create intance
        # gain property voice in pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 125) # set speed
        engine.setProperty('voice', voices[16].id) # set prononcment en_us
        engine.say(audio)
        engine.runAndWait()
        
    def recognize(self):
        # create intance
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            print("Say something sir...")
            # listen from microphone
            audio = r.listen(source)
        try:
            print("Recognizing...")
            self.speak("Recognizing...")
            # reconize microphone online with google
            Query = r.recognize_google(audio, language='en-in')
            print("You said : ", Query)
            return Query
            
        except Exception as e:
            print(e)
            print("Say that again sir")
            return Query
    
recogition = Assist()
recogition.speak("Hello Im ANGAB your virtual assistent")
OG = recogition.recognize().lower()
if "open google" in OG:
    print("Opening Google")
    webbrowser.get("/usr/bin/firefox").open("www.google.com")
    