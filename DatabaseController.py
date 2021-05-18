import mysql.connector
import os
import hashlib

db = None
cursor = None

def fetch_db_creds():
    with open(os.path.join('resources', 'dbCreds')) as file: 
        token = file.readline()
    return token.split(',')

def connect_database():
    global db
    global cursor
    creds = fetch_db_creds()
    db = mysql.connector.connect(
            host=creds[0],
            user=creds[1],
            password=creds[2],
            database=creds[3]
        )
    cursor = db.cursor()
    
def insert_keyword(server, user, keyword):
    global cursor
    cursor.execute(
        "replace into Users (id, userId, serverName, keyString) values (%(id)s, %(userId)s, %(serverName)s, %(keyString)s)", 
        {
            'id': generate_id(user, server),
            'userId':  str(user),
            'serverName': server,
            'keyString': keyword
        }
    )
    db.commit()
        
def fetch_server_keywords(server):
    global cursor
    cursor.execute(
    "select userId, keyString from Users where serverName=%(server)s",
        {
            'server': server
        }
    )
    return cursor.fetchall()
    
def print_table():
    global cursor
    cursor.execute("select * from Users")
    for x in cursor.fetchall():
        print(x)
        
def generate_id(user, server):
    toHash = str(user) + str(server)
    return hashlib.md5(toHash.encode()).hexdigest()
