#import libraries
import requests
import configFunction as cf
import json
import os

#get endpoints
endpoints = requests.get("https://www.courtlistener.com/api/rest/v3/")
endpoints = endpoints.json()

TOKEN = cf.tokenOut()

masterList={}
endScript = ");"
sep = " "

# change field names to postgresql syntax
textFields = ['field', 'nested object', 'string', 'slug', 'file upload', 'url', 'email', 'choice']
smallIntFields = ['integer']
timeStampFields = ['datetime']

for key, value in endpoints.items():
    TOKEN = cf.tokenOut()
    tablename = key
    url = value
    options = requests.options(url, headers={'Authorization': TOKEN})
    try:
        optionsDict = options.json()['actions']['POST']
    except:
        print('no data types found in: '+ tablename)
    fieldList = ["CREATE TABLE",tablename,"("]
    for key, value in optionsDict.items():
        fieldList.append(key)
        if value['type'] in textFields:
            dtype = 'text'
        elif value['type'] in smallIntFields:
            dtype = 'smallint'
        elif value['type'] in timeStampFields:
            dtype = 'timestamp'
        else:
            dtype = value['type']
        fieldList.append(dtype)
        fieldList.append(",")
    fieldList.pop()
    fieldList.append(endScript)
    tableScript = sep.join(fieldList)
    masterList[tablename] = tableScript

with open('createTableScripts.json', 'w') as fp:
    json.dump(masterList, fp)
