from datetime import datetime
from speak import speak


def getTime():
    currentTime = datetime.now()

    return str(currentTime.hour) + "hour" + str(currentTime.minute) + "minute"


def wishMe():
    hour = datetime.now().hour

    if 0 <= hour <= 12:
        speak("good Morning sir")

    elif 12 < hour <= 18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")

    speak("My name is jarvis. how may i help you")
