import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    #      it wishes you as soon as you enter
   
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >=12 and hour <18:
        speak("Good AfterNoon")

    else:
        speak("Good Evening!")

    speak("Im Jarvis . How may I assist you?")


def takeCommand():

 # it takes microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print (f"User said :{query}\n")

    except Exception  as e:

        print("Say that again please")
        return "None"
    return query


    # def sendEmail(to,content):
    #     server =smtplib.SMTP('smtp.gmail.com',587)
    #     server.ehlo()
    #     server.starttls()
    #     server.login('youremail@gmail.com','your-password')
    #     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    #logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query :
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\Users\piyus\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile(codePath)

        # elif 'email to shrek' in query:
        #     try:
        #         speak("What should I say")
        #         content = takeCommand()
        #         to = "shrek@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry wasnt able to send the email")



