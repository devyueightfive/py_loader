import os.path
import shutil
import unittest

from core.database.initialization import initializeDatabase, settings, saveSettings


class databaseSuite(unittest.TestCase):
    def setUp(self):
        pass

    def test_AbsenceOfPathToDatabaseInSettings(self):
        # force change 'pathToDatabase' to ''
        saveSettings('pathToDatabase', '')
        oldDatabase = settings['pathToDatabase']
        self.assertEqual(oldDatabase, '', 'Blank path is not created for "pathToDatabase".')
        # create database with default parameters
        newDatabase = initializeDatabase()
        self.assertEqual(os.path.join(os.path.abspath('.'), settings['defaultPathToDatabase']),
                         newDatabase, 'Database is created with no defaultPathToDatabase')

    def test_AbsenceOfDatabase(self):
        # force delete 'pathToDatabase'
        oldDatabase = os.path.dirname(settings['pathToDatabase'])
        if os.path.exists(oldDatabase):
            shutil.rmtree(oldDatabase)
        self.assertEqual(os.path.exists(oldDatabase), False, 'Database is not removed.')
        # create database with default parameters
        newDatabase = initializeDatabase()
        self.assertEqual(os.path.join(os.path.abspath('.'), settings['defaultPathToDatabase']),
                         newDatabase, 'Database is created with no defaultPathToDatabase')


if __name__ == '__main__':
    unittest.main()
