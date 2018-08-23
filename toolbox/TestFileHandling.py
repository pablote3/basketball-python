import unittest
import os
from Fnc_FileHandling import FncFileHandling


class TestFileHandling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.abs_path = "/home/pablote/git/basketball-python/toolbox/files"      #absolute path
        cls.rel_path = os.path.dirname(__file__) + "/files"                     #relative working directory

    def test_read_file(self):
        self.assertEqual(2, FncFileHandling.read_line(self.abs_path + '/paulRead.txt'))
        self.assertEqual(2, FncFileHandling.read_line(self.rel_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FncFileHandling.read_line(self.rel_path + '/paulo.txt'))
        self.assertEqual('line1\nline2', FncFileHandling.read_string(self.rel_path + '/paulRead.txt', 0))
        self.assertEqual('line', FncFileHandling.read_string(self.rel_path + '/paulRead.txt', 4))
        self.assertEqual('openFailed', FncFileHandling.read_string(self.rel_path + '/paulo.txt', 0))

    def test_append_write(self):
        self.assertEqual(4, FncFileHandling.append_line(self.abs_path + '/paulAppend.txt', "\nAppended"))    #exists
        self.assertEqual(2, FncFileHandling.append_line(self.abs_path + '/paulAppender.txt', "\nAppended"))  #not exist

    @classmethod
    def tearDownClass(cls):
        FncFileHandling.remove_line(cls.abs_path + '/paulAppend.txt', "\nAppended")
        FncFileHandling.delete_file(cls.rel_path + '/paulAppender.txt')
