import mysql.connector


def findAnswer(command):
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jarvis"
    )

    mycursor = mydatabase.cursor()
    mycursor.execute("select * from founder")
    for x in mycursor.fetchall():
        if x[0] in command:
            answer = x[1]
            positiveResponse = x[2]
            negativeResponse = x[3]
            return [answer, positiveResponse, negativeResponse]





