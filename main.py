import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk

engine = pyttsx3.init()
voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150)
engine.say("I will speak this text")
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def command():
    content = " "
    while content == " ":  
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)    
        # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio)
            print("You said: " + r.recognize_google(audio))
        except Exception as e:
            print("please try again")
            
    return content  
def main_process():    
    while True:   
        request = command().lower()
        if "hello" in request:
            speak("Welcome, how can I help you today.") 
        elif "play my favourite music" in request:
            speak("Playing music for you.")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://youtu.be/G5knFtrWaR4?si=70cSsoosdS2M18qF")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=LsoLEjrDogU")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=fLexgOxsZu0")
        elif "say time" in request:
                now_time = datetime.datetime.now().strftime("%H:%M:")
                speak("current time is " + str(now_time))
        elif "youtube" in request:
            webbrowser.open("https://www.youtube.com")        
        elif "open" in request:
            query = request.replace("open ","")
            pyautogui.press("super")
            pyautogui.typewrite(query) 
            pyautogui.press("enter")   
        elif "wikipedia" in request:
            request = request.replace("nikhil","")
            request = request.replace("search wikipedia","")      
            result = wikipedia.summary(request, sentences = 2)
            print(result)
            speak(result)
        elif "google" in request:
            request = request.replace("nikhil","")
            request = request.replace("search google","") 
            webbrowser.open("https://www.google.com/search?q=" + request)
        elif "send whatsapp" in request:
            pwk.sendwhatmsg_instantly("+91XXXXXXXXXX","Hello from Nikhil",15,True,2)

           

           
main_process()