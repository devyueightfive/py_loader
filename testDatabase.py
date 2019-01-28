import os.path
import unittest
import shutil

import preparations


class databaseSuite(unittest.TestCase):
    def setUp(self):
        pass

    def test_AbsenceOfPathToDatabaseInSettings(self):
        # force change 'pathToDatabase' to ''
        preparations.saveSettings('pathToDatabase', '')
        oldDatabase = preparations.settings['pathToDatabase']
        self.assertEqual(oldDatabase, '', 'Blank path is not created for "pathToDatabase".')
        # create database with default parameters
        newDatabase = preparations.prepareDatabase()
        self.assertEqual(os.path.join(os.path.abspath('.'), preparations.settings['defaultPathToDatabase']),
                         newDatabase, 'Database is created with no defaultPathToDatabase')

    def test_AbsenceOfDatabase(self):
        # force delete 'pathToDatabase'
        oldDatabase = os.path.dirname(preparations.settings['pathToDatabase'])
        shutil.rmtree(oldDatabase)
        self.assertEqual(os.path.exists(oldDatabase), False, 'Database is not removed.')
        # create database with default parameters
        newDatabase = preparations.prepareDatabase()
        self.assertEqual(os.path.join(os.path.abspath('.'), preparations.settings['defaultPathToDatabase']),
                         newDatabase, 'Database is created with no defaultPathToDatabase')


if __name__ == '__main__':
    unittest.main()
