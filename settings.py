import json

from tables import IsDescription, Float32Col, Int32Col, StringCol

settings = None


# load settings from 'settings.json'
def loadSettings():
    linkToSettingsFile = open('settings.json', mode='r')
    global settings
    settings = json.load(linkToSettingsFile)
    linkToSettingsFile.close()


def saveSettings(key, value):
    global settings
    settings[key] = value
    linkToSettingsFile = open('settings.json', mode='w')
    json.dump(settings, linkToSettingsFile)
    linkToSettingsFile.close()


# initialize settings


# settings for database structure
class DescriptionForTradesTable(IsDescription):
    price = Float32Col()
    amount = Float32Col()
    timestamp = Float32Col()
    tid = Int32Col()
    type = StringCol(3)


loadSettings()
