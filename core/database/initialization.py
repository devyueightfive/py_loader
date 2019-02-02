import os.path
import re

import tables

from core.settings import settings, saveSettings, DescriptionForTradesTable


# create database with parameters from settings.json
def createDefaultDatabase():
    # use default path to database.
    defaultPathToDatabase = os.path.join(os.path.abspath('.'), settings['defaultPathToDatabase'])
    pathToDatabase = os.path.dirname(defaultPathToDatabase)
    # In case of absence database
    if not os.path.exists(pathToDatabase):
        os.makedirs(pathToDatabase)
    # create new database.
    with tables.open_file(filename=defaultPathToDatabase, mode='w', title='Crypto Trades') as hdf5Base:
        # Use settings.json parameters for database structure.
        # Pathes to tables will be as /TRADEPAIR/MARKETURL
        for pair in settings['tradePairs']:
            pairGroup = hdf5Base.create_group('/', pair)
            for mu in settings['marketURLs']:
                urlGroup = hdf5Base.create_group(pairGroup, mu.replace('.', ''))
                table = hdf5Base.create_table(urlGroup, 'trades', DescriptionForTradesTable,
                                              title="Trades")
                table.close()
    # //end with

    # Save new parameters in settings.json.
    saveSettings('pathToDatabase', defaultPathToDatabase)
    # //end if

    # Return new parameter for tests
    return defaultPathToDatabase


# Checking existence of database.
# In case of absence create new one.
def initialization():
    # Get path to database from settings.json.
    fullPathToDatabase = settings['pathToDatabase']
    # In case of wrong path to database
    if not os.path.isfile(path=fullPathToDatabase):
        pattern = re.compile('[yY]')
        agree = pattern.match(input(f'File {fullPathToDatabase} is not found. '
                                    f'Do you want to create database with default parameters?'))
        if agree:
            createDefaultDatabase()
        else:
            exit(0)
