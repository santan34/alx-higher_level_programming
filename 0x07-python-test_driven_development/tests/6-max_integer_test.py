#!/usr/bin/python3
"""
Unit test for for the function def max_integer(list=[]):
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class test_maxint(unittest.TestCase):

    def test1(self):
        self.assertEqual(max_integer([1, 3, 5]), 5)
        self.assertEqual(max_integer([5, 3]), 5)

    def test2(self):
        self.assertEqual(max_integer([]), None)

    def test3(self):
        self.assertRaises(TypeError, max_integer, 0)

    def test4(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test5(self):
        self.assertRaises(KeyError, max_integer, {2:'b', 1:'d'})

    def test6(self):
        self.assertEqual(max_integer('hell'), 'l')

    def test7(self):
        self.assertEqual(max_integer([-2, -4, -6]), -2)

if __name__ == "__main__":
    unittest.main()

