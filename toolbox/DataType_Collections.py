import unittest


class DataTypeCollections(unittest.TestCase):
    def test_listSlicing(self):
        slice1 = ['a', 'b', 'c']
        self.assertEqual(3, len(slice1))                #length of list
        self.assertEqual('c', slice1[2])
        self.assertEqual('b', slice1[1])
        self.assertEqual('a', slice1[0])
        self.assertEqual('c', slice1[-1])               #last element
        self.assertEqual('b', slice1[-2])               #next to last

        self.assertEqual(['a', 'b', 'c'], slice1[0:3])
        self.assertEqual(['b', 'c'], slice1[1:3])
        self.assertEqual(['a', 'b'], slice1[:2])        #from start to 2
        self.assertEqual(['a', 'b', 'c'], slice1[:3])   #from start to 3
        self.assertEqual(['b', 'c'], slice1[1:])        #from 2 to end
        self.assertEqual(['c'], slice1[2:])             #from 3 to end
        self.assertEqual(['a', 'b', 'c'], slice1[:])    #copy entire list

    def test_listMethods(self):
        methods1 = ['a', 'b', 'c']
        methods1.append('a')			                #add to end of list
        self.assertEqual(4, len(methods1))
        self.assertEqual('a', methods1[0])
        self.assertEqual('a', methods1[3])
        self.assertEqual('a', methods1[-1])             #last element

        self.assertEqual(0, methods1.index('a'))
        self.assertEqual(0, methods1.index('a', 0))
        self.assertEqual(3, methods1.index('a', 1))
        self.assertEqual(2, methods1.count('a'))

        methods1[3] = 'z'    				            #replace list element
        self.assertEqual('z', methods1[3])

        methods1.remove('z')
        self.assertEqual(3, len(methods1))
        self.assertRaises(IndexError, lambda: methods1[3])


if __name__ == '__main__':
    unittest.main()
