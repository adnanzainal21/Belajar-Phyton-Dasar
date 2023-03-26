import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing NDIL")

Master = "Andi"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning" + Master)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + Master)
    else :
        speak("Good Evening" + Master)
        speak("") 
        
#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again please")
        query = None
        
    return query
        
#main program
speak("Hello my name is deal, i can help you!")
wishMe()
query = takeCommand()

#Logic for task as por query
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)
    
if "I'm bored" in query.lower():
    game = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam %s"
    print(game)
elif "open youtube" in query.lower():
    url = "youtube.com"
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    webbrowser.get(edge_path).open(url)
elif "open google" in query.lower():
    url = "google.com"
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    webbrowser.get(edge_path).open(url)
elif "find my phone" in query.lower():
    input("Your Number Phone = ")
    url = "https://www.google.com/android/find"
    edge_path = "C:/Users/Lenovo/AppData/Local/Programs/Opera/launcher.exe %s"
    webbrowser.get(edge_path).open(url)
elif "the time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"(Master) the time is (strTime)")
