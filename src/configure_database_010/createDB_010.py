import psycopg2
from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import configFunction as cf

filename = "database.ini"
dbName = 'postgresql'

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
cur.execute('SELECT version()')
version = cur.fetchone()
print(version)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
createDB = 'CREATE DATABASE CourtListener;'
cur.execute(createDB)
conn.close()
