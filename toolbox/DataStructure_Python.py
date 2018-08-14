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

        methods1.insert(1, 'red')                       #insert at specific index
        self.assertEqual('red', methods1[1])
        methods1.pop(1)
        self.assertEqual('b', methods1[1])              #remove from specific index

        self.assertEqual(0, methods1.index('a'))
        self.assertEqual(0, methods1.index('a', 0))
        self.assertEqual(3, methods1.index('a', 1))
        self.assertEqual(2, methods1.count('a'))

        methods1[3] = 'z'    				            #replace list element
        self.assertEqual('z', methods1[3])

        methods1.remove('z')
        self.assertEqual(3, len(methods1))
        self.assertRaises(IndexError, lambda: methods1[3])

    def test_listSort(self):
        sort1 = ["hello", "1", "True", "-.5"]
        self.assertEqual('hello', sort1[0])
        sort1.sort()
        self.assertEqual('-.5', sort1[0])

    def test_listNumbers(self):
        numbers1 = [3, -5, .6, 17000, 7]
        self.assertEqual(-5, min(numbers1))
        self.assertEqual(17000, max(numbers1))

    def test_listRange(self):
        range1 = range(5)
        self.assertEqual(range(0, 5), range1)
        self.assertEqual([0, 1, 2, 3, 4], list(range1))

    def test_listFromTuple(self):
        tup1 = ('foo', 'bar', 'baz')
        list1 = list(tup1)
        self.assertEqual(['foo', 'bar', 'baz'], list1)
        list1[1] = 'peep'
        self.assertEqual(['foo', 'peep', 'baz'], list1)

    def test_tupleSimple(self):
        tup1 = 4, 5, 6, 5
        self.assertEqual((4, 5, 6, 5), tup1)
        self.assertEqual(2, tup1.count(5))              #number of occurrences of a value

    def test_tupleNested(self):
        tup1 = (4, 5, 6), (7, 8)
        self.assertEqual(((4, 5, 6), (7, 8)), tup1)     #nested tuples

    def test_tupleString(self):
        tup1 = tuple('string')
        self.assertEqual(('s', 't', 'r', 'i', 'n', 'g'), tup1)
        self.assertEqual('s', tup1[0])

    def test_tupleConcatenate(self):
        tup1 = (4, None, 'foo') + (6, 0) + ('bar', )
        self.assertEqual((4, None, 'foo', 6, 0, 'bar'), tup1)

    def test_tupleAssignmentUnpacking(self):
        tup1 = (4, 5, 6)
        a, b, c = tup1
        self.assertEqual(4, a)
        self.assertEqual(5, b)
        self.assertEqual(6, c)

    def test_tupleIterateOverSequences(self):
        tup1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        i = 0
        for a, b, c in tup1:
            if i == 0:
                self.assertEqual(1, a)
                self.assertEqual(2, b)
            elif i == 1:
                self.assertEqual(4, a)
                self.assertEqual(5, b)
            else:
                self.assertEqual(7, a)
                self.assertEqual(8, b)
            i += 1


if __name__ == '__main__':
    unittest.main()
