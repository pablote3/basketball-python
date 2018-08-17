import unittest


class DataTypeCollections(unittest.TestCase):
    def test_listSlicing(self):
        slice1 = ['a', 'b', 'c']
        self.assertEqual(3, len(slice1))                #length of list
        self.assertEqual('c', slice1[2])
        self.assertEqual('b', slice1[1])
        self.assertEqual('a', slice1[0])
        self.assertEqual('c', slice1[-1])               #last element, slice relative to the end
        self.assertEqual('b', slice1[-2])               #next to last

        self.assertEqual(['a', 'b', 'c'], slice1[0:3])
        self.assertEqual(['b', 'c'], slice1[1:3])
        self.assertEqual(['a', 'b'], slice1[:2])        #from start to 2
        self.assertEqual(['a', 'b', 'c'], slice1[:3])   #from start to 3
        self.assertEqual(['b', 'c'], slice1[1:])        #from 2 to end
        self.assertEqual(['c'], slice1[2:])             #from 3 to end
        self.assertEqual(['a', 'b', 'c'], slice1[:])    #copy entire list

        slice1[1:3] = ['d', 'e']                        #assign using sequence
        self.assertEqual(list(['a', 'd', 'e']), slice1)

    def test_listMethods(self):
        methods1 = ['a', 'b', 'c']
        methods1.append('a')			                #add to end of list
        self.assertEqual(4, len(methods1))
        self.assertEqual('a', methods1[0])
        self.assertEqual('a', methods1[3])
        self.assertEqual('a', methods1[-1])             #last element

        methods1.insert(1, 'red')                       #insert at specific index - slow, move all other indexes
        self.assertEqual('red', methods1[1])
        methods1.pop(1)                                 #remove from specific index - slow, move all other indexes
        self.assertEqual('b', methods1[1])

        self.assertEqual(0, methods1.index('a'))        #find first value
        self.assertEqual(0, methods1.index('a', 0))     #find value with starting index
        self.assertEqual(3, methods1.index('a', 1))
        self.assertEqual(2, methods1.count('a'))        #count number of values
        self.assertEqual(True, 'a' in methods1)         #list contains value - slow, scan entire list
        self.assertEqual(True, 'k' not in methods1)

        methods1[3] = 'z'    				            #replace list element
        self.assertEqual('z', methods1[3])

        methods1.remove('z')                            #removes first instance of value
        self.assertEqual(3, len(methods1))
        self.assertRaises(IndexError, lambda: methods1[3])

        methods1.extend([5, 'b'])                       #add items to existing list
        self.assertEqual(5, len(methods1))

    def test_listSort(self):
        sort1 = ["hello", "1", "True", "-.5"]
        self.assertEqual('hello', sort1[0])
        sort1.sort()                                    #sort existing list alphabetically
        self.assertEqual(list(['-.5', '1', 'True', 'hello']), sort1)
        sort1.sort(key=len)                             #sort existing list by length
        self.assertEqual(list(['1', '-.5', 'True', 'hello']), sort1)

        sort2 = sorted(["hello", "1", "True", "-.5"])   #create sorted list
        self.assertEqual(list(['-.5', '1', 'True', 'hello']), sort2)

        sort3 = reversed(["hello", "1", "True", "-.5"])  #create list in reverse order
        self.assertEqual(list(['-.5', 'True', '1', 'hello']), list(sort3))

    def test_listNumbers(self):
        numbers1 = [3, -5, .6, 17000, 7]
        self.assertEqual(-5, min(numbers1))
        self.assertEqual(17000, max(numbers1))

    def test_listRange(self):
        range1 = range(5)
        self.assertEqual(range(0, 5), range1)
        self.assertEqual([0, 1, 2, 3, 4], list(range1))

    def test_listZip(self):
        list1 = ['foo', 'bar', 'baz']
        list2 = ['one', 'two', 'three']
        zipped1 = zip(list1, list2)                       #pair up elements from two lists
        self.assertEqual([('foo', 'one'), ('bar', 'two'), ('baz', 'three')], list(zipped1))

        list3 = ['one', 'two']
        zipped2 = zip(list1, list3)                       #pair up elements from two lists using shortest sequence
        self.assertEqual([('foo', 'one'), ('bar', 'two')], list(zipped2))

    def test_listFromTuple(self):
        tup1 = ('foo', 'bar', 'baz')
        list1 = list(tup1)
        self.assertEqual(['foo', 'bar', 'baz'], list1)
        list1[1] = 'peep'
        self.assertEqual(['foo', 'peep', 'baz'], list1)

    def test_listComprehension(self):
        list1 = ['a', 'as', 'bat', 'car', 'dove', 'python']
        list2 = [x.upper() for x in list1 if len(x) > 2]    #filter and transform elements
        self.assertEqual(['BAT', 'CAR', 'DOVE', 'PYTHON'], list2)

    def test_dictMethods(self):
        dict1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
        self.assertEqual({'a': 'some value', 'b': [1, 2, 3, 4]}, dict1)
        self.assertEqual([1, 2, 3, 4], dict1['b'])

        dict1['c'] = 9                                  #insert new key
        dict1[7] = 'an integer'
        self.assertEqual({'a': 'some value', 'b': [1, 2, 3, 4], 'c': 9, 7: 'an integer'}, dict1)
        self.assertEqual(True, 'b' in dict1)            #check if key exists
        del dict1['a']                                  #delete using key
        self.assertEqual({'b': [1, 2, 3, 4], 'c': 9, 7: 'an integer'}, dict1)
        ret = dict1.pop(7)                              #delete using key and return value
        self.assertEqual({'b': [1, 2, 3, 4], 'c': 9}, dict1)
        self.assertEqual('an integer', ret)

        self.assertEqual(2, len(list(dict1.keys())))    #return iterator of dict keys
        self.assertEqual(2, len(list(dict1.values())))  #return iterator of dict values

        dict2 = {'x': 'another value', 'y': 4}
        dict1.update(dict2)                             #merge one dict into another
        self.assertEqual({'b': [1, 2, 3, 4], 'c': 9, 'x': 'another value', 'y': 4}, dict1)
        dict3 = {'x': 'new value'}
        dict1.update(dict3)                             #merge with override of existing value
        self.assertEqual({'b': [1, 2, 3, 4], 'c': 9, 'x': 'new value', 'y': 4}, dict1)

        self.assertEqual(9, dict1.get('c', 'Tree'))     #use default if key not found
        self.assertEqual('Tree', dict1.get('g', 'Tree'))

    def test_dictFromSequences(self):
        key1 = range(5)
        value1 = reversed(range(5))
        dict1 = dict(zip(key1, value1))                 #create dict from sequences
        self.assertEqual({0: 4, 1: 3, 2: 2, 3: 1, 4: 0}, dict1)

    def test_setMethods(self):
        set1 = {2, 2, 2, 1, 3, 3, 4, 5}                 #create set with set keyword
        self.assertEqual({1, 2, 3, 4, 5}, set1)
        set2 = {4, 4, 5, 7, 6, 8, 3, 3}                 #create set with curly braces
        self.assertEqual({3, 4, 5, 6, 7, 8}, set2)

        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, set1.union(set2))    #returns distinct elements from either sets
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8}, set1 | set2)
        self.assertEqual({3, 4, 5}, set1.intersection(set2))            #returns elements occurring in both sets
        self.assertEqual({3, 4, 5}, set1 & set2)

        set1.add(6)                                     #add element to set
        self.assertEqual({1, 2, 3, 4, 5, 6}, set1)
        set1.remove(6)                                  #remove element from set
        self.assertEqual({1, 2, 3, 4, 5}, set1)
        set1.pop()                                      #remove arbitrary element from set
        self.assertEqual({2, 3, 4, 5}, set1)

        set2.clear()                                    #reset set to empty
        self.assertEqual(set(), set2)

    def test_setSubset(self):
        set1 = {1, 2, 3, 4, 5}
        self.assertEqual(True, {1, 2, 3}.issubset(set1))
        self.assertEqual(True, set1.issuperset({1, 2, 3}))

    def test_setComprehension(self):
        set1 = {'a', 'as', 'bat', 'car', 'dove', 'python'}
        set2 = {len(x) for x in set1}                   #transform elements
        self.assertEqual({1, 2, 3, 4, 6}, set2)
        set3 = set(map(len, set1))                      #transform elements using map
        self.assertEqual({1, 2, 3, 4, 6}, set3)

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
