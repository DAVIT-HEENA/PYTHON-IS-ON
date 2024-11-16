# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#
# while 1:
#     print("enter a word")
#     s= input()
#     speaker.Speak(s)
from time import strftime
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import datetime
import os
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=  1
        audio = r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "some error Occured . sorry from aod ai"

if __name__ == '__main__':
    print("pycham")
    say("hello I am aod A.I ")
    while True:
        print("Listening...")
        text= takecommand()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["spotify","https://open.spotify.com/"]]
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])
        if "exit".lower() in text.lower():
            say("have a nice day sir good bye")
            exit()
        if "the time".lower() in text.lower():
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir time is {strfTime}")
        if "play music".lower() in text.lower():
            path = "C:/Users/MY PC/Downloads/flute.mp3"
            os.startfile(path)
        if "open vs code".lower() in text.lower():
            path = "C:/Users/MY PC/OneDrive/Desktop/Visual Studio Code.lnk"
            os.startfile(path)


