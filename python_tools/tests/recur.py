#!/usr/bin/python
import unittest
import sys
import os

def subSandwich_new(word, char):
    num = word.count(char)
    if num ==0:
        return 0
    elif num ==1:
        return len(char)
    else:
        # first string with length of char
        first = word[:len(char)]

        match = 0
        if first == char:
            match = match + 1
        else:
            # remove 1 char from word
            word = word[1:]
        # string from end with the length of char
        last = word[-len(char):]
        if last == char:
            match = match + 1
        else:
            # removing 1 char from word
            word = word[:-1]
        if match ==2:
            # first and last both match
            return len(word)
        else:
            return subSandwich_new(word, char)

class SandwichTestNew(unittest.TestCase):
    def test_subSandwich_new(self):
        word = 'catcowcat'
        result = subSandwich_new(word, 'cat')
        self.assertEqual(result, 9)

    def test_subSandwich_new2(self):
        word = 'catcowcat'
        result = subSandwich_new(word, 'cow')
        self.assertEqual(result, 3)

    def test_subSandwich_new3(self):
        result = subSandwich_new('ccatcowcatxx', 'cat')
        self.assertEqual(result, 9)

    def test_subSandwich_new4(self):
        result = subSandwich_new('cat', 'cat')
        self.assertEqual(result, 3)

    def test_subSandwich_new5(self):
        result = subSandwich_new('cat', 'cow')
        self.assertEqual(result, 0)


def subSandwich(word, char, pos, start, end):
    if pos == len(word) -1:
        if end == 0:
            return len(char)
        return end -(start -2)

    if word[pos:pos+len(char)] == char:
        if start != 0:
            end = pos + len(char) - 1
        else:
            start = pos + 1
    return subSandwich(word, char, pos + 1, start, end)


class SandwichTest(unittest.TestCase):
    def test_subSandwich(self):
        result = subSandwich('catcowcat', 'cat', 0, 0, 0)
        self.assertEqual(result, 9)

        result = subSandwich('catcowcat', 'cow', 0, 0, 0)
        self.assertEqual(result, 3)


        result = subSandwich('ccatcowcatxx', 'cat', 0, 0, 0)
        self.assertEqual(result, 9)
        result = subSandwich('cat', 'cat', 0, 0, 0)
        self.assertEqual(result, 3)
        result = subSandwich('cat', 'cow', 0, 0, 0)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(SandwichTest)
    suite = unittest.TestLoader().loadTestsFromTestCase(SandwichTestNew)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
