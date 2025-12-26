#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install SpeechRecognition pyttsx3')
get_ipython().system('pip install sounddevice')


# In[2]:


import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import scipy.io.wavfile as wav
import tempfile

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    duration = 5  # seconds
    fs = 16000    # sampling rate

    print("🎙️ How can I help you Boss...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Save to temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, fs, recording)
        recognizer = sr.Recognizer()
        with sr.AudioFile(f.name) as source:
            audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        speak(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that Boss.")
        return ""


# In[3]:


listen()


# In[4]:


engine = pyttsx3.init('sapi5')


# In[5]:


engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Max volume



# In[6]:


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use first available voice


# In[7]:


import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"🔊 Speaking: {text}")
    engine.say(text)
    engine.runAndWait()


# In[8]:


speak("Hello Rishi, your assistant is now speaking!")


# In[9]:


import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import scipy.io.wavfile as wav
import tempfile
import os

# Initialize Snarky's voice
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print(f"🔊 Snarky says: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    import sounddevice as sd
    import scipy.io.wavfile as wav
    import tempfile
    import speech_recognition as sr

    duration = 8
    fs = 16000
    sd.default.device = 1

    print("🎙️ Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("✅ Recording complete.")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, fs, recording)
        recognizer = sr.Recognizer()
        with sr.AudioFile(f.name) as source:
            audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ Raw transcription: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Didn't catch that, Rishi. Try again?")
        return ""


def respond_to_command(command):
    if is_snarky_called(command):
        speak("Hi Rishi, Snarky here.")
    if "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
    elif "open youtube" in command or "search youtube" in command:
        speak("Opening YouTube.")
        import webbrowser
        webbrowser.open("https://www.youtube.com")
    elif "hello" in command:
        speak("Hello Rishi! Ready to roll.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye Rishi. Snarky signing off.")
        return False
    else:
        speak("I'm not sure what you mean, but I'm listening.")
    return True

def is_snarky_called(command):
    trigger_words = ["snarky", "smart key", "snarkie", "snacky", "ladki", "sonakshi", "anarchy"]
    return any(word in command for word in trigger_words)


# In[13]:


command = listen()
respond_to_command(command)


# In[14]:


print(f"🗣️ You said: {command}")


# In[15]:


from IPython.display import Audio
Audio("snarky_test.wav")


# In[ ]:





# In[16]:


speak("Hi Rishi, Snarky here.")


# In[17]:


while True:
    command = listen()
    if "exit" in command or "stop" in command:
        speak("Goodbye Rishi. Snarky signing off.")
        break
    elif "snarky" in command:
        speak("Hi Rishi, Snarky here.")
    elif "open notepad" in command:
        speak("Opening Notepad.")
        import os
        os.system("notepad.exe")
    else:
        speak("I'm not sure what you mean, but I'm listening.")


# In[18]:


print("📂 Launching:", "python C:\\Users\\Rishi\\OneDrive\\Desktop\\snarky.py")


# In[ ]:





# In[ ]:




