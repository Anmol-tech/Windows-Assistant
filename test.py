import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 110)
engine.say('hello world')
engine.runAndWait()