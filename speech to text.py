import pyttsx3
import speech_recognition as sr
import wikipedia as wiki
import webbrowser 
import os
import pywhatkit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def takecommand():
   
   r= sr.Recognizer()
   with sr.Microphone() as source:
       print("listining")
       r.pause_threshold = 1
       r.energy_threshold = 300
       audio = r.listen(source,0,4)
   try:
       print("recognizing")
       query = r.recognize_google(audio, language='en-in')
       print(f"yash said:{query}\n")

   except Exception as e: 
       print("say that again ")  
       return "none"  
   return query


if __name__ == "__main__":
    while True:
        query = takecommand().lower()



