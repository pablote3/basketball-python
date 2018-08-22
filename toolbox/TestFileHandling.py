import unittest
import os
from FileHandling import FileHandling


class TestFileHandling(unittest.TestCase):
    def test_read_file(self):
        absolute_path = "/home/pablote/git/basketball-python/toolbox"
        relative_path = os.path.dirname(__file__)       #absolute working directory
        self.assertEqual(2, FileHandling.function_read_line(absolute_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(absolute_path + '/paulo.txt'))
        self.assertEqual(2, FileHandling.function_read_line(relative_path + '/paulRead.txt'))
        self.assertEqual('openFailed', FileHandling.function_read_line(relative_path + '/paulo.txt'))
        self.assertEqual('line1\nline2', FileHandling.function_read_string(relative_path + '/paulRead.txt', 0))
        self.assertEqual('line', FileHandling.function_read_string(relative_path + '/paulRead.txt', 4))
        self.assertEqual('openFailed', FileHandling.function_read_string(relative_path + '/paulo.txt', 0))
