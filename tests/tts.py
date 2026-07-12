import pyttsx3

engine = pyttsx3.init()

text = input("Type something: ")

engine.say(text)

engine.runAndWait()