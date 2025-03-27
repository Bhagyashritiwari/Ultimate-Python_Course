import speech_recognition as sr 
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine= pyttsx3.init()


def speak (text):
    engine.say(text)
    engine.runAndWait( )

if __name__ == "__main__":
    speak("Hello, Bhagyashri Tiwari I am here to assist you?, "
    "As i know your petname is Bani so Bani are you making AI model for your personal staff to do"
    "i am happy to help you as i am AI model and i am good to create your emails and share data information")
