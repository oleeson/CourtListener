import json
import configFunction as cf
import psycopg2
import os

with open('createTableScripts.json', 'r') as file:
    scriptDict = json.load(file)

#create one long script
masterList = []
sep = '\n'
for key, value in scriptDict.items():
    masterList.append(value)
masterScript = sep.join(masterList)
masterScript = masterScript.replace(" user ", ' "user" ')

#connect to database
filename = 'database.ini'
dbName = 'courtlistener'
owd = os.getcwd()

try:
    os.chdir("../../config/")
    path = os.getcwd() + "/" + filename
    print("Path to file: ", path)
    print("dbName: ", dbName)
    os.chdir(owd)
except:
    path = input("input path to db configuration file: ")

config = cf.config(path, dbName)
conn = psycopg2.connect(**config)
cur = conn.cursor()
cur.execute(masterScript)

#check it worked
check = " SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"
cur = conn.cursor()
cur.execute(check)
for record in cur:
    print (record)

conn.close()
print("connection closed")
