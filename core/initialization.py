import os.path

import tables

from core.settings import settings, saveSettings, DescriptionForTradesTable


# Checking existence of database.
# In case of absence create new one.
def initializeDatabase():
    # Get path to database from settings.json.
    fullPathToDatabase = settings['pathToDatabase']
    # In case of wrong path to database
    if not os.path.isfile(path=fullPathToDatabase):
        # use default path to database.
        fullPathToDatabase = os.path.join(os.path.abspath('.'), settings['defaultPathToDatabase'])
        pathToDatabase = os.path.dirname(fullPathToDatabase)
        # In case of absence database
        if not os.path.exists(pathToDatabase):
            os.makedirs(pathToDatabase)
        # create new database.
        with tables.open_file(filename=fullPathToDatabase, mode='w', title='Crypto Trades') as hdf5Base:
            # Use settings.json parameters for database structure.
            for pair in settings['tradePairs']:
                pairGroup = hdf5Base.create_group('/', pair)
                for mu in settings['marketURLs']:
                    urlGroup = hdf5Base.create_group(pairGroup, mu.replace('.', ''))
                    table = hdf5Base.create_table(urlGroup, 'trades', DescriptionForTradesTable,
                                                  title="Trades")
                    table.close()
        # //end with

        # Save new parameters in settings.json.
        saveSettings('pathToDatabase', fullPathToDatabase)
    # //end if

    # Return new parameter for tests
    return fullPathToDatabase


def initialize():
    initializeDatabase()
