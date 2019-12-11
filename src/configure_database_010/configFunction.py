from configparser import ConfigParser
from getpass import getpass
import os

## Get parameters for database connection from .ini file
def config(pathToFile, dbName):
    parser = ConfigParser()

    try:
        parser.read(pathToFile)
    except:
        print(pathToFile + "path not found")

    dbDict = {}

    try:
        parser.has_section(dbName)
    except:
        print('DB {0} not found in the {1} file'.format(dbName, pathToFile))
    params = parser.items(dbName)
    for param in params:
            dbDict[param[0]] = param[1]

    return dbDict

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
