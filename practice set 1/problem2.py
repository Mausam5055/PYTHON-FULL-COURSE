# Q:INSTALL AN EXTERNAL MODULE OF YOUR INTREST 
# AND USE IT TO PERFORM  AN OPERATION

import pyttsx3
engine = pyttsx3.init()
engine.say("hey mausam what are you doing ")
engine.runAndWait()



# EXPLAINATION:
'''
1.pyttsx3 is a text-to-speech conversion library in Python.
Unlike alternative libraries, it works offline, 

2.Installation:
pip install pyttsx3(Write this in terminal to install this module)

3.Usage :
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
(write this command in vs code)


4.Changing Voice , Rate and Volume :
-----------
import pyttsx3
engine = pyttsx3.init() # object creation

5.""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


6."""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

7."""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

8."""Saving Voice to a file"""
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
'''