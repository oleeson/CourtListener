import psycopg2
from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import configFunctions as cf

filename = "database.ini"
dbName = 'postgresql'

conn = cf.connect(filename, dbName)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
createDB = 'CREATE DATABASE CourtListener;'
cur = conn.cursor()
cur.execute(createDB)
conn.close()
