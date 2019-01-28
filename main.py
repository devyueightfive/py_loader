import os
import tables
from settings import pathToDatabase, DescriptionForTradesTable, \
    tradePairs, marketURLs


def prepareDatabase():
    if not os.path.isfile(path=pathToDatabase):
        with tables.open_file(filename=pathToDatabase, mode='w', title='Crypto Trades') as h5base:
            'create groups'
            for pair in tradePairs:
                pairGroup = h5base.create_group('/', pair)
                for mu in marketURLs:
                    urlGroup = h5base.create_group(pairGroup, mu.replace('.', ''))
                    table = h5base.create_table(urlGroup, 'trades', DescriptionForTradesTable, title="Trades")
                    table.close()


def makePreparations():
    prepareDatabase()


def makeMainCycle():
    pass


# Body of Main program
makePreparations()
makeMainCycle()
