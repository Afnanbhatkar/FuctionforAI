import pyttsx3
import datetime
import pyttsx3
import speech_recognition as sr
import emoji

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate',180)

def Speak(Text):
     Assistant.say(Text)
     print(f"AI : {Text}")
     Assistant.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      Speak('Good morning sir..')
      print(emoji.emojize(":smiling_face_with_smiling_eyes:"))

    elif hour>=12 and hour<18:
     Speak('Good Afternoon sir..')
     print(emoji.emojize(":smiling_face_with_smiling_eyes:"))

    else:
      Speak('Good Evening Sir..')
      print(emoji.emojize(":smiling_face_with_smiling_eyes:"))
  
wishMe()