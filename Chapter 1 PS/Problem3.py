#3. Install an external module and use it to perform an operation of your interest. 

#Ans- use pyTTSX3 engine use , this module use for text to speak

import pyttsx3
engine = pyttsx3.init()
engine.say("Hi Bhagyashri Tiwari, I am text to speak ")

engine.runAndWait()


# Why Use This Syntax?
# import pyttsx3: Imports the library so you can use its functions.
# engine = pyttsx3.init(): Initializes the text-to-speech engine so you can configure it and control how it speaks.
# engine.say(text): Queues the text to be spoken. You can queue multiple pieces of text to be spoken in sequence if needed.
# engine.runAndWait(): Processes the queued text and blocks execution until speaking is finished. This ensures that all the text is spoken before the program proceeds or terminates.
# This sequence of commands is a typical pattern for using the pyttsx3 library to perform text-to-speech conversion in a Python script.