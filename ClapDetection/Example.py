import pyttsx3
import speech_recognition as sr
from ClapDetection.ClapDetection import Tester

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate',180)

def Speak(Text):
     print('', '')
     Assistant.say(Text)
     print(f"AI : {Text}")
     Assistant.runAndWait()

def  Commadtaker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('')
        print('  : Listening sir...')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,6)
 
    try:
        print('  : Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print('')
        print(f'You:{query}\n')

 
    except Exception as e: 
        print('  : Say that again please...')
        return ""
    return query
    

def Tasks():
    
    while True:
        Query = Commadtaker().lower()
        if "Hello" in Query:
            Speak("Heyy there. how are you?")
            
        elif "bye" in Query:
            Speak("Bye! have a nice day.")
            break
            
        else:
            pass

def ClapDetection():
    
    Query = Tester()
    if "True-Mic" in Query:
        print("")
        Speak("Welcome back Sir !! How may i help you")
        print("")
        Tasks() 
        
ClapDetection()