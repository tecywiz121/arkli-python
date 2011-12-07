#!/usr/bin/env python
import unittest
from arkli.signature import quote_rfc3986

class TestQuoteFunction(unittest.TestCase):
    def test_none(self):
        '''
        Test encoding a basic string with no special characters
        '''
        test = 'this_is-a~test'
        result = quote_rfc3986(test)
        self.assertEqual(result, test)

    def test_space(self):
        '''
        Tests encoding a string with a space
        '''
        test = 'space here'
        result = quote_rfc3986(test)
        self.assertEqual(result, 'space%20here')

    def test_at(self):
        '''
        Tests encoding an @ symbol
        '''
        test = 'at@here'
        result = quote_rfc3986(test)
        self.assertEqual(result, 'at%40here')

if __name__ == '__main__':
    unittest.main()
