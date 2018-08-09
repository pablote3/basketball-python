import unittest


class DataTypeCollections(unittest.TestCase):

    def test_list(self):
        my_list = ['a', 'b', 'c']
        self.assertEqual(3, len(my_list))
        self.assertEqual('a', my_list[0])
        #my_list[-1]				'c'		last element
        #my_list[-2]				'b'		next to last


if __name__ == '__main__':
    unittest.main()
