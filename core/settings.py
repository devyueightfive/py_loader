import json
import os.path
import sys

import tables

settings = None

settingsFileName = os.path.abspath('.') + '/core/settings.json'

if not os.path.exists(settingsFileName):
    print('No such file "./core/settings.json" .')
    sys.exit(1)


# load settings from 'settings.json'
def loadSettings():
    linkToSettingsFile = open(settingsFileName, mode='r')
    global settings
    settings = json.load(linkToSettingsFile)
    linkToSettingsFile.close()


def saveSettings(key, value):
    global settings
    settings[key] = value
    linkToSettingsFile = open(settingsFileName, mode='w')
    json.dump(settings, linkToSettingsFile)
    linkToSettingsFile.close()


# initialize settings


# settings for database structure
class DescriptionForTradesTable(tables.IsDescription):
    price = tables.Float32Col()
    amount = tables.Float32Col()
    timestamp = tables.Float32Col()
    tid = tables.Int32Col()
    type = tables.StringCol(3)


loadSettings()
