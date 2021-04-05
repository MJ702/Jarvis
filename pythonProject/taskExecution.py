import os
import sys
import socket
import webbrowser
from time import sleep
from instagram import api
import database
from takeCommand import takeCommand
import time_module
from speak import speak
import instagram
import spacy

nlp = spacy.load("en_core_web_lg")


def taskExecution():
    followingList = instagram.getFollowingList()
    followersList = instagram.getFollowersList()

    while True:
        command = input("Enter your command: ")

        try:
            if 'what is time' in command or 'tell me time' in command:
                speak(f'Time is{time_module.getTime()}')

            elif "how many following" in command:
                speak(f"you following {len(followingList)} person")

            elif "open following list" in command or 'show my following list':
                i = 1
                test = open('test.txt', 'w+')
                for following in followingList:
                    test.write(f"{i}) {following}" + '\n')
                    i = i + 1

                speak("Open following list")
                os.startfile('test.txt')
                test.close()

            elif "how many followers" in command or 'how many people follow me':
                followersList = instagram.getFollowersList()
                speak(f"{len(followersList)} people follow you sir")

            elif "open followers list" in command or 'show my follower list':
                i = 1
                test = open('test.txt', 'w+')
                for follower in followersList:
                    test.write(f"{i}) {follower}" + '\n')
                    i = i + 1

                speak("Showing follower list")
                os.startfile('test.txt')
                test.close()

            elif 'set private account' in command:
                if api.setPrivateAccount():
                    speak("your account is now private.")

            elif 'set public account' in command:
                if api.setPublicAccount():
                    speak("your account is now public")

            elif 'sleep jarvis' in command:
                speak("ok sir, as your wise")
                break

            elif 'follow' in command:
                command = command.replace('follow', '')
                command = command.replace(' ', '')
                name = command.split(' ')[-1]
                followersList = instagram.getFollowingList()
                if name in followersList:
                    speak(f'sir already follow{name}')
                    break

                api.searchUsers(name)
                result = api.LastJson
                pkNumber = [user['pk'] for user in result['users']]
                pkNumber = pkNumber[0]
                if api.follow(pkNumber):
                    speak(f"now your are follow {name}")
                else:
                    speak('sir, username in not found')

            elif 'remove' in command:
                command = command.replace('remove', '')
                command = command.replace(' ', '')
                name = command.split(' ')[-1]
                if name not in followingList:
                    speak(f"you not follow {name}")
                else:
                    api.searchUsers(name)
                    result = api.LastJson
                    try:
                        pkNumber = [user['pk'] for user in result['users']]
                        pkNumber = pkNumber[0]

                        if api.unfollow(pkNumber):
                            speak(f"{name} in not your following list")

                    except:
                        speak('i cannot find username')

            elif 'check internet connection' in command:
                ipaddress = socket.gethostbyname(socket.gethostname())
                if ipaddress == "127.0.0.1":
                    speak(answer[2])
                else:
                    speak(answer[1])

            elif 'open' in command:
                if 'chrome' in command or 'google' in command:
                    webbrowser.open("chrome")
                    speak("opening chrome")

                if 'notepad' in command:
                    os.startfile("Notepad")
                    speak("opening notepad")

                if 'control panel' in command:
                    os.system("cmd /c control panel")
                    speak("opening control panel")

                if 'open folder' in command:
                    speak("which folder i open for you")
                    folderName = input("Enter your folder name: ")

                    path = ["C:/", "D:/", "E:/"]
                    folderList = list()
                    for i in path:
                        for root, dirs, files in os.walk(i):
                            for f in dirs:
                                if folderName in f.lower():
                                    temp = os.path.join(root, f)
                                    folderList.append(temp)

                    if len(folderList) > 1:
                        speak(f"i found many directory of {folderName} folder, can i show list")
                        answer = input("Enter you answer: ")
                        if answer in "yes":
                            for i in folderList:
                                print('\t' + i)
                            sleep(len(folderList) / 2)
                            speak("which directory i open")
                            index = int(input("enter your index number")) - 1
                            os.startfile(folderList[index])

                        else:
                            speak("ok sir")
                    elif len(folderList) == 0:
                        speak("i can not found folder")

                    elif len(folderList) == 1:
                        os.startfile(folderList[0])

                if 'open file' in command:
                    speak("which file i open for you")
                    folderName = input("Enter your folder name: ")

                    path = ["C:/", "D:/", "E:/"]
                    folderList = list()
                    for i in path:
                        for root, dirs, files in os.walk(i):
                            for f in files:
                                if folderName in f.lower():
                                    temp = os.path.join(root, f)
                                    folderList.append(temp)

                    if len(folderList) > 1:
                        speak(f"i found many file of {folderName} folder, can i show list")
                        answer = input("Enter you answer: ")
                        if answer in "yes":
                            for i in folderList:
                                print('\t' + i)
                            sleep(len(folderList) / 2)
                            speak("which file i open")
                            index = int(input("enter your index number")) - 1
                            os.startfile(folderList[index])

                        else:
                            speak("ok sir")
                    elif len(folderList) == 0:
                        speak("i can not found folder")

                    elif len(folderList) == 1:
                        os.startfile(folderList[0])

            elif 'goodbye jarvis' in command:
                speak(answer[1])
                sys.exit()

        except:
            speak("i don't understand your command")
