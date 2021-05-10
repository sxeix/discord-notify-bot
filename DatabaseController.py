import mysql.connector
import os

db = None
cursor = None

def fetchDbCreds():
    with open(os.path.join('resources', 'dbCreds')) as file: 
        token = file.readline()
    return token.split(',')

def connectDatabase():
    global db
    global cursor
    creds = fetchDbCreds()
    db = mysql.connector.connect(
            host=creds[0],
            user=creds[1],
            password=creds[2],
            database=creds[3]
        )
    cursor = db.cursor()
    
def printTable():
    global cursor
    cursor.execute("select * from Users")
    for x in cursor.fetchall():
        print(x)
    