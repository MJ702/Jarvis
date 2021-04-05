from taskExecution import taskExecution
from takeCommand import takeCommand
import sys
from time_module import wishMe
from speak import speak

if __name__ == '__main__':
    # wishMe()
    while True:
        

#         this is the comment
        taskExecution()
        permission = takeCommand()

        if 'wake up' in permission:
            speak("I am ready sir what can i do for you")
            taskExecution()

        elif 'goodbye' in permission:
            speak("goodbye sir, see you again")
            sys.exit()
