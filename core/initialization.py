import os.path

import tables

from core.settings import settings, saveSettings, DescriptionForTradesTable


def initializeDatabase():
    fullPathToDatabase = settings['pathToDatabase']
    if not os.path.isfile(path=fullPathToDatabase):
        fullPathToDatabase = os.path.join(os.path.abspath('.'), settings['defaultPathToDatabase'])
        pathToDatabase = os.path.dirname(fullPathToDatabase)
        if not os.path.exists(pathToDatabase):
            os.makedirs(pathToDatabase)
        with tables.open_file(filename=fullPathToDatabase, mode='w', title='Crypto Trades') as hdf5Base:
            'create groups'
            for pair in settings['tradePairs']:
                pairGroup = hdf5Base.create_group('/', pair)
                for mu in settings['marketURLs']:
                    urlGroup = hdf5Base.create_group(pairGroup, mu.replace('.', ''))
                    table = hdf5Base.create_table(urlGroup, 'trades', DescriptionForTradesTable,
                                                  title="Trades")
                    table.close()
        # end with

        # save settings in settings.json
        saveSettings('pathToDatabase', fullPathToDatabase)
    # return value  for tests
    return fullPathToDatabase


def initialize():
    initializeDatabase()
