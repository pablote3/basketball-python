import unittest
import os
from FileHandling import FileHandling


class TestFileHandling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.absolute_path = "/home/pablote/git/basketball-python/toolbox/files"
        cls.relative_path = os.path.dirname(__file__) + "/files"       #absolute working directory

    def test_read_file(self):
        self.assertEqual(2, FileHandling.function_read_line(self.absolute_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(self.absolute_path + '/paulo.txt'))
        self.assertEqual(2, FileHandling.function_read_line(self.relative_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(self.relative_path + '/paulo.txt'))
        self.assertEqual('line1\nline2', FileHandling.function_read_string(self.relative_path + '/paulRead.txt', 0))
        self.assertEqual('line', FileHandling.function_read_string(self.relative_path + '/paulRead.txt', 4))
        self.assertEqual('openFailed', FileHandling.function_read_string(self.relative_path + '/paulo.txt', 0))

    def test_append_write(self):
        self.assertEqual(4, FileHandling.function_append_add(self.absolute_path + '/paulAppend.txt'))
#        self.assertEqual("complete", FileHandling.function_append_add(self.absolute_path + '/paulWrite.txt'))

    @classmethod
    def tearDownClass(cls):
        FileHandling.function_append_remove(cls.absolute_path + '/paulAppend.txt')


