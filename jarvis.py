import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
import datetime
import cv2
import random

import wikipedia
import webbrowser
import sys
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Convert voice into text
def Takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=15, phrase_time_limit=15)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again, please...")
        return "none"
    return query

# Get current time
def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The running time is")
    speak(t)

# Wish the user
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis, sir. Please tell me how can I help you")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)   
    server.ehlo()
    server.starttls()
    server.login("kadamroshan5050@gmail.com", "softwareengineer")
    server.sendmail("kadamroshan5050@gmail.com", to, content)
    server.close()

# Main function
if __name__ == "__main__":
    wish()
    while True:
        query = Takecommand().lower()

        if "open notepad" in query:
            path1 = "C:\\Windows\\notepad.exe"
            os.startfile(path1)

        elif "close notepad" in query:
            speak("Okay sir, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "time" in query:
            time()

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")
                
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open microsoft edge" in query:
            path2 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(path2)

        elif "open cmd" in query:
            path3 = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(path3)

        elif "open control panel" in query:
            path4 = "C:\\Windows\\system32\\control.exe"
            os.startfile(path4)

        elif "open calculator" in query:
            path9 = "C:\\Windows\\System32\\calc.exe"
            os.startfile(path9)

        elif "open word" in query:
            path5 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path5)

        elif "open powerpoint" in query:
            path6 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path6)

        elif "open excel" in query:
            path7 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path7)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "c:\\Users\\Aakash\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            speak(results)

        elif "play song on youtube" in query:
            kit.playonyt("See You Again")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = Takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        # To set an alarm
        elif "set alarm" in query:
            speak("Enter the time!")
            alarm_time = input("Enter the time in HH:MM:SS format: ")
            
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == alarm_time:
                    speak("Time to wake up, sir!")
                    playsound("D:\\project\\python gui\\Personal Assistant\\musin0\\trap-future-bass-royalty-free-music-167020.mp3")
                    speak("Alarm closed!")
                    break

        # Send email
        elif "send email" in query:
            try:
                to = "ds5864065@gmail.com"
                speak("What should I send?")
                content = Takecommand()
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send the email.")

        # WhatsApp message
        elif "whatsapp" in query:
            from whatsapp import sendMessage
            sendMessage()

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        else:
            speak("Sorry sir, I did not understand that.")
        
        speak("Sir, do you have any other task?")
