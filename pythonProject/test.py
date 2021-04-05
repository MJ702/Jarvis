import os
from speak import speak
from time import sleep

folderName = 'Jarvis'
folderName = folderName.lower()


path = ["C:/", "D:/", "E:/"]
folderList = list()
for i in path:
    for root, dirs, files in os.walk(i):
        for f in dirs:
            if folderName in f.lower():
                temp = os.path.join(root, f)
                folderList.append(temp)

print(folderList)
# if len(folderList) > 1:
#     speak(f"i found many directory of {folderName} folder, can i show list")
#     answer = input("Enter you answer: ")
#     if answer in "yes":
#         print(folderList)
#         sleep(len(folderList) / 2)
#         speak("which directory i open")
#         index = int(input("enter your index number")) - 1
#         os.startfile(folderList[index])
#
#     else:
#         speak("ok sir")
#
# else:
#     os.startfile(folderList[0])
