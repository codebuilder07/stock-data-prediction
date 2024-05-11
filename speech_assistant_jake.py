
# speaking Assistance Application

import speech_recognition as sr    #pip install speechRecognition
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import yfinance as yf
import ssl
import certifi
import time
import os
import datetime

  
class User:
    def __init__(self,name):
        self.name=name
user1=User(name="")
class SpeechAName:
    def __init__(self,name):
        self.name=name
speech1=SpeechAName(name="Jake")

def there_exists(terms):
    for term in terms:
        if term.lower()in voice_data.lower():
            print(term)
            return True


r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        speak('Speak now')
    #Using the with statement in this context ensures 
    #that the microphone is properly initialized and closed, even if an exception occurs within the code block.
    #It's a clean and concise way to handle resources with automatic acquisition and release
        r.adjust_for_ambient_noise(source)
        audio= r.listen(source)
        try:
            voice_data=r.recognize_google(audio)
            #voice_data1=r.recognize_google_cloud(audio)
            
        except sr.UnknownValueError:
            speak('i didn\'t get that')
        except sr.RequestError:
            speak(' Service is down')
        print(voice_data)
        #print(voice_data1)
        return(voice_data)




def speak(audio_string):
    tts=gTTS(audio_string,lang="en")
    r=random.randint(0,200000)    
    audio="audio"+str(r)+".mp3"  # naming the audiofile
    tts.save(audio)
    playsound.playsound(audio)
    print(f"Jake: {audio_string}")
    os.remove(audio)
def respond(voice):
    if there_exists(['hey','hi','hello']):
        greeting=[f'how are you doing {user1.name}',f'hey what\'s up {user1.name}',f'i\'m listening {user1.name}']
        greet=(greeting[random.randint(0,len(greeting)-1)])
        speak(greet)
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if user1.name=="":
            speak(f' My name is {speech1.name}. what\'s your?')
        else:
            speak(f' My name is {speech1.name}.')

    elif there_exists(["my name is"]):
        person_name=voice.split("is")[-1].strip()
        user1.name=person_name
        speak(f'i will remember the name {person_name}')
    elif there_exists(["how are you","how are you doing"]):
        speak(f"i'm doing well. thanks for asking {user1.name}")
    elif there_exists(["what's the time","tell me the time","what time is it", "what is the time"]):
        time=ctime().split()[3].split(":")[0:2]
        speak(f'time is {time[0]}:{time[1]}')
    elif there_exists(["search for"]) and 'youtube' not in voice:
        search_term=voice.split("for")[-1]
        url=f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'This is what i found for {search_term} in google')
        
    elif there_exists(["youtube"]):
        search_term= voice.split("for")[-1]
        print(search_term)
        url=f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    elif there_exists(["price of"]):
        search_term= voice.lower().split("of")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        start = datetime.datetime(2010, 1, 1)
        end = datetime.datetime(2022, 12, 31)
        try:
            stock1=stocks[search_term]
            speak(stock1)
            ticker = yf.Ticker(stock1) 
            df = ticker.history(start=start, end=end)
            speak(f'{df["Open"][0]}')
        except:
            speak('oops, something went wrong')
    elif there_exists(["exit", "quit", "goodbye"]):
       speak("going offline")
       exit()


time.sleep(1)
while(1):
    voice_data=record_audio()
    respond(voice_data)
    

