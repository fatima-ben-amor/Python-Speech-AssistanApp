import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            fatima_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            fatima_speak('Sorry, I did not get that')
        except sr.RequestError:
            fatima_speak('Sorry, my speech service is down')
        return voice_data


def fatima_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        fatima_speak('My name is Fatima')
    if 'what time is it' in voice_data:
        fatima_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do u want to search about !')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        fatima_speak('here is what I found' +search)
    if 'find location' in voice_data:
        location = record_audio('what location u search about !')
        url = 'https://www.google.tn/maps/place/' + location + '&/amp;'
        webbrowser.get().open(url)
        fatima_speak('here is what I found for ' + location)
    if 'find profile' in voice_data:
        profile = record_audio('what profile u search about !')
        url = 'https://www.linkedin.com/in/' + profile
        webbrowser.get().open(url)
        fatima_speak('here is what I found for ' + profile)
    if 'find video' in voice_data:
        video = record_audio('what video u search about !')
        url = 'https://www.youtube.com/results?search_query=' + video
        webbrowser.get().open(url)
        fatima_speak('here is what I found for ' + video)
    if 'stop' in voice_data:

        exit()
        fatima_speak('ok I will exit with love')



time.sleep(1)
fatima_speak('How can i help u?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
