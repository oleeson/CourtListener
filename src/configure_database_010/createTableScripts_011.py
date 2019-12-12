#import libraries
import requests
import configFunction as cf
import json
import os

#get endpoints
endpoints = requests.get("https://www.courtlistener.com/api/rest/v3/")
endpoints = endpoints.json()
del endpoints["recap"]

TOKEN = cf.tokenOut()

masterList={}
endScript = ");"
sep = " "

# change field names to postgresql syntax
textFields = ['field', 'nested object', 'string', 'slug', 'file upload', 'url', 'email', 'choice']
smallIntFields = ['integer']
timeStampFields = ['datetime']

for key, value in endpoints.items():
    tablename = key
    tablename = tablename.replace("-", "_")
    url = value
    options = requests.options(url, headers={'Authorization': TOKEN})
    fieldList = ["CREATE TABLE",tablename,"("]
    try:
        optionsDict = options.json()['actions']['POST']
        print('table script for '+tablename+' created')
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
    except:
        print('no data types found in: '+ tablename + '... all dtypes will be read in as text.')
        try:
            req = requests.get(url, headers={'Authorization': TOKEN})
            resultsDict = req.json()['results'][0]
            for key in resultsDict:
                fieldList.append(key)
                fieldList.append('text')
                fieldList.append(',')
        except:
            print('not Authorized to return results for '+tablename+" table.")
    fieldList.pop()
    fieldList.append(endScript)
    tableScript = sep.join(fieldList)
    masterList[tablename] = tableScript

with open('createTableScripts.json', 'w') as fp:
    json.dump(masterList, fp)
