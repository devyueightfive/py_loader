import json
from tables import IsDescription, Float32Col, Int32Col, StringCol
from os.path import curdir, join

# load settings from 'settings.json'
linkToSettingsFile = open('settings.json', mode='r')
settings = json.load(linkToSettingsFile)

# initialize settings

# path to database
pathToDatabase = join(curdir, settings['pathToDatabase'])


# settings for database structure
class DescriptionForTradesTable(IsDescription):
    price = Float32Col()
    amount = Float32Col()
    timestamp = Float32Col()
    tid = Int32Col()
    type = StringCol(3)


# general market settings
tradePairs = settings['tradePairs']
marketURLs = settings['marketURLs']
