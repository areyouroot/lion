import speech_recognition as sr # nessary files for speech_recognition
import pyttsx3 # python text to speech files
import pywhatkit # to have feature like access youtube etc
import datetime # time
import wikipedia # wikipedia
import pyjokes #some predifined jokes
from playsound import playsound # to play any audio file

listener = sr.Recognizer() #to enable microphone access
engine = pyttsx3.init() # text to speech engine
voices = engine.getProperty('voices') 
engine.setProperty('rate',170)
engine.setProperty('voice', voices[1].id) #changing features of speech 


#this is automation of text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()


#main code 
def run_lion():

    playsound('./sound.mp3') #indication beep
    print("tell me")
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'lion' in command: #few filters
            command = command.replace('lion', '')
            print(command)
        print(command)
    if 'play' in command: #plays songs in youtube
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command: #says time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command: #wiki search
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command: #jokes
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')



talk("hello my name is lion and how can i help you") #greetings

while True:

    run_lion()
    