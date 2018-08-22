import unittest
import os
from FileHandling import FileHandling


class TestFileHandling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.absolute_path = "/home/pablote/git/basketball-python/toolbox"
        cls.relative_path = os.path.dirname(__file__)       #absolute working directory

    def test_read_file(self):
        self.assertEqual(2, FileHandling.function_read_line(self.absolute_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(self.absolute_path + '/paulo.txt'))
        self.assertEqual(2, FileHandling.function_read_line(self.relative_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(self.relative_path + '/paulo.txt'))
        self.assertEqual('line1\nline2', FileHandling.function_read_string(self.relative_path + '/paulRead.txt', 0))
        self.assertEqual('line', FileHandling.function_read_string(self.relative_path + '/paulRead.txt', 4))
        self.assertEqual('openFailed', FileHandling.function_read_string(self.relative_path + '/paulo.txt', 0))

    def test_read_write(self):
        self.assertEqual(2, FileHandling.function_read_line(self.absolute_path + '/paulRead.txt'))