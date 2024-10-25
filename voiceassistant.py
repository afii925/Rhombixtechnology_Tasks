## Voice Assistant
# pip install wolphrame
# pip install pyttsx3 
#pip install wikipedia
#pip install SpeechRecognition
#pip install ecapture

## Importing Libraries 

import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Sir!")
    elif hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    assname = "Alexa"
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you, sir?")
    uname = takeCommand()
    speak("Welcome Afzaal")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    
    speak("How can I help you, Sir?")

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
        print(e) 
        print("Unable to recognize your voice.") 
        return "None"
    
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        
        # Enable low security in Gmail
        server.login('your_email@gmail.com', 'your_email_password')  # Update with your email credentials
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to YouTube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding!")
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = r"C:\Users\AFZAAL MUSTAFA\Desktop\DSA LAB TASKS\DSA lab-4 Task\songs"
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver_email@example.com"  # Update with actual receiver email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send?")
                to = takeCommand()  # Get email address via voice
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, thank you.")
            speak("How are you, Sir?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine.")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir?")
            assname = takeCommand()
            speak("Thanks for naming me.")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Gaurav.")

        elif "calculate" in query: 
            app_id = "Wolframalpha API ID"  # Replace with your actual API ID
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "").strip()
            webbrowser.open(query) 

        elif "who am i" in query:
            speak("If you talk, then definitely you're human.")

        elif "why you came to world" in query:
            speak("Thanks to Gaurav. Further, it's a secret.")

        elif 'power point presentation' in query:
            speak("Opening PowerPoint presentation.")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is the 7th sense that destroys all other senses.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav.")  

        elif 'reason for you' in query:
            speak("I was created as a minor project by Mister Gaurav.")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully.")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:
            try: 
                jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=your_api_key_here')  # Update with your API key
                data = json.load(jsonObj)
                i = 1
                
                speak('Here are some top news from the Times of PAKISTAN:')
                print('''=============== TIMES OF PAKISTAN ============''' + '\n')
                
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1 
            except Exception as e:
                print(str(e))
                speak("Could not fetch news.")

        elif 'lock window' in query:
            speak("Locking the device.")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold on a sec! Your")


