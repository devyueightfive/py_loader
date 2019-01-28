import os.path

import tables

from settings import settings, saveSettings, DescriptionForTradesTable


def prepareDatabase():
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
        saveSettings('pathToDatabase', fullPathToDatabase)
    return fullPathToDatabase


def makePreparations():
    prepareDatabase()


if __name__ == '__main__':
    makePreparations()
