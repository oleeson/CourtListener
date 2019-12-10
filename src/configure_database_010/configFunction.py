from configparser import ConfigParser

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
