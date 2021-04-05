import os


folderName = "takeCommand"
path = ["C:/", "D:/", "E:/"]
folderList = list()
for i in path:
    for root, dirs, files in os.walk(i):
        for f in files:
            if folderName in f:
                temp = os.path.join(root, f)
                folderList.append(temp)

print(folderList)