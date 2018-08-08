import unittest


class PythonConditions(unittest.TestCase):
    def test_if(self):
        self.assertEqual("Greater", condition_if(34, 33))
        self.assertEqual("Equal", condition_if(34, 34))
        self.assertEqual("Less", condition_if(34, 35))

    def test_for(self):
        self.assertEqual(3, condition_for(["apple", "banana", "cherry"]))
        self.assertEqual(2, condition_for(["apple", "banana"]))
        self.assertEqual(1, condition_for(["apple"]))
        self.assertEqual(0, condition_for([]))

    def test_range(self):
        self.assertEqual(10, condition_range(5))
        self.assertEqual(8, condition_range(4))

    def test_while(self):
        self.assertEqual(0, condition_while(5))
        self.assertEqual(1, condition_while(4))
        self.assertEqual(2, condition_while(3))
        self.assertEqual(2, condition_while(2))


if __name__ == '__main__':
    unittest.main()


def condition_if(int1, int2):
    if int1 > int2:
        return "Greater"
    elif int1 < int2:
        return "Less"
    else:
        return "Equal"


def condition_for(fruits):
    i = 0
    for _ in fruits:
        i += 1
    return i


def condition_range(int1):
    i = 0
    for x in range(int1):
        i += 2
    return i


def condition_while(int1):
    i = 0
    while int1 < 5:
        int1 += 1
        i += 1
        if i == 2:
            break
    return i
