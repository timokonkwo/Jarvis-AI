import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import smtplib
from time import sleep
import webbrowser as web
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
# name = input("Enter your name: ")
# speak('hello')

def time():
    Time = datetime.datetime.now().strftime("%I:%H:%S")
    speak("Ok sir, The Current time is")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("ok sir, The Current date is")

    speak(day)
    speak(month)
    speak(year)
# date()

def greet():
    speak("Welcome to Mr. Tim's Intelligent Support")
    # time()
    # date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak('Good Morning Sir!')
    elif hour >= 12 and hour <= 18:
        speak('Good afternoon sir!')
    elif hour >= 18 and hour <= 24:
        speak('Good Evening Sir')
    else:
        speak('Good Night sir!')

    speak('How may i help you today?')
greet()

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Speak Sir\nI am Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.record(source, duration=2)
        #listens for the user's input
        # audio = r.listen(source)

    try:
        print("\nRecognizing your speech...")
        query = r.recognize_google(audio, language='en-Us')
        print(query)
        speak(query)

    except Exception as e:
        print(e)
        speak("I couldn't get what you said sir")

        return "None"

    return query

def email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("okonkwotim00@gmail.com", '07034668957@tim')
    server.sendmail("okonkwotim00@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Tim/Pictures/AI/screen.png")
    print('I have taken the screenshot sir')
    speak('I have taken the screenshot sir')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('The CPU usage is at' + usage)

    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    print(f'The Battery percent is {percent}%')
    speak("The battery of your computer is at "+ percent + " Percent")



def jokes():
    myJokes = pyjokes.get_joke()
    speak(myJokes)
    print(myJokes)


if __name__ == "__main__":
    greet()
    while True:
        sleep(1)
        query = take().lower()

        print(query)

        if "time" in query:
            time()

        elif "training" in query:
            speak('Yes sir. I know about the One month Training!')
            sleep(2)
            speak('I am Python Sir. I already know how to code!')

        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Ok sir, I am going offline now, Bye bye")
            quit()
        elif "shut" in query:
            speak("ok sir, i will be shutting down your laptop shortly!!!, Bye bye")
            os.system("shutdown /s /t 4")

        elif "log out" in query:
            speak('ok sir, I am locking your Laptop now!')
            os.system('shutdown -l')

        elif "restart" in query:
            speak('Ok sir, I am restarting your laptop now!')
            os.system('shutdown /r /t 5')

        elif 'song' in query:
            speak("ok sir, i will play a song for you now")
            songs_path = "C:\\Users\\Tim\\Music\\" \
                         "Emma"
            songs = os.listdir(songs_path)
            os.startfile(os.path.join(songs_path, songs[0]))

        elif "wikipedia" in query:
            speak("ok sir, I am searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak('I have completed the search sir')
            sleep(2)
            print(result)
            speak(result)

        elif "tell me about" in query:
            speak("ok sir. Digitech is an Online Tech Hub which trains, develops and equips individuals with Neccessary and Profitable Technological Skills, which are needed for the twenty-first century.")

        elif "send email" in query:
            try:
                speak("ok sir, what message should i send?")
                sleep(2)
                content = take()
                speak("ok sir, i am sending it to him.")
                to = "okonkwotim01@gmail.com"
                email(to, content)
                speak('I have sent the email sir')
            except Exception as e:
                print(e)
                speak("I am unable to send the Email sir")
        elif "search" in query:
            speak("what should i search sir?")
            chromepath = 'C:/Users/Tim/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/internet explorer'#"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google chrome.exe"  #"C:\\Program Files\\Internet Explorer\\iexplore.exe"
            search = take().lower()
            web.get(chromepath).open_new_tab(search + ".com")

        elif 'remember' in query:
            speak('what should i remember sir?')
            data = take()
            data = data.replace('remember', '')
            speak('Ok sir, i will remember' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'remind me' in query:
            remember = open('data.txt', 'r')
            speak('you told me to remember' + remember.read())

        elif 'screenshot' in query:
            screenshot()

        elif "who is Tim" in query:
            speak("Tim is a programmer. He is a web developer too and he built me")

        elif 'battery' in query:
            cpu()

        elif 'joke' in query:
            jokes()