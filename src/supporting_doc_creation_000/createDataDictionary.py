#import required libraries
import requests
import json
import pandas as pd
from getpass import getpass
import os
from configparser import ConfigParser

## Define Funtions:
## Function retrieve token
def tokenOut(passwordFile = 'passwords.ini', section='olivia', passwordTo='api'):
    owd = os.getcwd()
    try:
        os.chdir('../../config/')
        path = os.getcwd()+"/"+passwordFile
    except:
        print('Path to passwords file not found. Please enter your path: ')
        path = input("Path to passwords.ini file: ")

    os.chdir(owd)
    parser = ConfigParser()
    parser.read(path)

    try:
        parser.has_section(section)
    except:
        print('Could not find section {} in password file: {}'.format(section, path))
        section = input("Please enter section header ie. 'YourName': ")
    params = parser.items(section)
    for param in params:
        if param[0] == passwordTo:
            Token = param[1]
            break
        else:
            continue
    nToken = "Token "+Token
    return nToken

## Function to create a help text table for all fields
## tablename: string
## endpointURL: API endpoint URL
def make_help_text_table(tablename,endpointURL,TOKEN):
    #get options
    options = requests.options(endpointURL,headers={'Authorization': TOKEN})
    try:
        main_dict = options.json()['actions']['POST']
        #get key name for inner dictionary
        field_keys = main_dict.keys()
        field_names = list(field_keys)

        # init empty lists
        field_name = []
        help_text = []

        # loop through fields and create two lists of fields and help text
        for field in field_names:
            try:
                main_dict[field]['help_text']
                field_name.append(field)
                help_text.append(main_dict[field]['help_text'])
            except:
                continue
        # create a dictionary to convert to pandas dataframe
        data = {'field_name':field_name, 'help_text':help_text}
        df = pd.DataFrame(data)
        df.insert(0, 'table', tablename)
        return df
    except:
        print (tablename, 'table actions key not found. table not included in output.')

# Function to create dataframe of results
def createDF():
    req = requests.get('https://www.courtlistener.com/api/rest/v3/')
    endpoints = req.json()
    frames = []
    for key, value in endpoints.items():
        tablename = key
        endpointURL = value
        try:
            frames.append(make_help_text_table(tablename, endpointURL, tokenOut()))
        except:
            print ("Error. Cannot append dataframe.")
    return frames

frames = createDF()

#concatenate all tables
result = pd.concat(frames)

#set path
owd = os.getcwd()
os.chdir("../../work_products")
path = os.getcwd()+'/datadictionary.csv'
os.chdir(owd)

#print to csv
result.to_csv(path)
