import speech_recognition as sr
from time import sleep


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listing...")
        audio = r.listen(source)

    try:
        print("Recognition....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print("say that again please...")
        return "None"

    return query.lower()