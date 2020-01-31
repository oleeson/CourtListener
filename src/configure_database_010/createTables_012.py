import json
import configFunctions as cf
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
conn = cf.connect()
cur = conn.cursor()
cur.execute(masterScript)

#check it worked
check = " SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';"
cur = conn.cursor()
cur.execute(check)
for record in cur:
    print (record)

conn.close()
print("connection closed")
