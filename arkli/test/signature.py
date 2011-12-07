#!/usr/bin/env python
import unittest
from arkli.signature import quote_rfc3986, create_signature

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

class TestSignatureFunction(unittest.TestCase):
    def test_blank(self):
        '''
        Tests signing a blank request
        '''
        result = create_signature('', '', '', '', 1, 'nonce');
        result = dict(result)
        self.assertIn('arkli_key', result)
        self.assertIn('arkli_nonce', result)
        self.assertIn('arkli_timestamp', result)
        self.assertIn('arkli_user', result)
        self.assertIn('arkli_signature', result)
        
        self.assertEqual(result['arkli_signature'],
                            'NJFLQn3cpfZM9gF+ESFKGFInFqg=')
    
    def test_no_email(self):
        '''
        Tests signing a standard request
        '''
        result = create_signature('key', 'secret', 'test-user', '', 1, 'nonce');
        result = dict(result)
        self.assertIn('arkli_key', result)
        self.assertIn('arkli_nonce', result)
        self.assertIn('arkli_timestamp', result)
        self.assertIn('arkli_user', result)
        self.assertIn('arkli_signature', result)
        
        self.assertEqual(result['arkli_signature'],
                            'SoPo6WtIERgfKTo9I/Z1wDQuNSU=')

if __name__ == '__main__':
    unittest.main()
