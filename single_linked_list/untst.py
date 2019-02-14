import unittest
from main_ import *

class TestList(unittest.TestCase):

    def test_create(self):
        list_0 = List(value=5, next_=List(value=6, next_=List(value=7)))
        self.assertEqual(str(list_0), '5 6 7')

    def test_append(self):
        list_1 = List(value=1, next_=List(value=2, next_=List(value=3)))
        self.assertEqual(list_1.append(4), '1 2 3 4')
        self.assertEqual(list_1.append(0), '1 2 3 4 0')

    def test_iadd(self):
        list_4 = List(value=1, next_=List(value=2, next_=List(value=3)))
        list_5 = List(value=4, next_=List(value=5, next_=List(value=6)))
        list_4 += list_5
        self.assertEqual(str(list_4), '1 2 3 4 5 6')
        list_5 += [7, 8]
        self.assertEqual(str(list_5), '4 5 6 7 8')

    def test_set_attr(self):
        list_6 = List(value=7, next_=List(value=6, next_=List(value=5, next_=List(value=4))))
        list_6._value = 0
        self.assertEqual(str(list_6), '0 6 5 4')
        list_7 = List(value=1, next_=List(value=2, next_=List(value=3)))
        list_7._value = 22
        self.assertEqual(str(list_7), '22 2 3')

    def test_reverse(self):
        list_2 = List(value=1, next_=List(value=2, next_=List(value=3)))
        self.assertEqual(list_2.print_reversed(), '3 2 1')
        list_2 = List(value=0, next_=List(value=3, next_=List(value=8, next_=List(value=5))))
        self.assertEqual(list_2.print_reversed(), '5 8 3 0')

    def test_iter(self):
        list_8 = List(value=1, next_=List(value=2, next_=List(value=3, next_=List(value=4))))
        array = []
        for elem in list_8:
            array.append(2**elem)
        self.assertEqual(' '.join([str(i) for i in array]), '2 4 8 16')


if __name__ == '__main__':
    unittest.main()
