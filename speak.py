#    METHOD TO CONVERT TEXT TO SPEECH 


''' METHOD 1 '''

#  pip install pyttsx3
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the text you want to convert to speech
text = input ("What do you wanna say..")

# Convert the text to speech
engine.say(text)

# Play the speech
engine.runAndWait()

'''  METHOD 2 '''
  
#  pip install gTTS
from gtts import gTTS

#  pip install os-sys
import os

# Ask the text you want to convert to speech
text = input ("What do you wanna say..")

# Create a gTTS object with the text
tts = gTTS(text)

# Save the audio file
tts.save("hello.mp3")

#  Play the audio file
os.system("hello.mp3")

''' METHOD 3 '''

#  pip install pyttsx3
import pyttsx3

#  pip install SpeechRecognition
import speech_recognition as sr 

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

#  change voice
voices = engine.getProperty('voices')

#  print the voice name 
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#  Define speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#  Set the text you want to convert to speech
text= input ("what do you wanna say") 

#  Speak the text as user wish
Speak (text)
