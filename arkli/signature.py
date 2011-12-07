#!/usr/bin/env python
import hmac
import hashlib
import time
import os
from base64 import b16encode, b64encode
import urllib
import re

def quote_rfc3986(url):
    '''
    Encodes a string according to rfc3986 percent encoding
    '''
    url = str(url)
    url = urllib.quote(url)
    url = url.replace('%7E', '~')
    return url

def urlencode_rfc3986(data):
    '''
    Encodes a dictionary into a query string using rfc3986 percent encoding for
    the keys and values.
    '''
    result = []
    for key, value in data:
        result.append(quote_rfc3986(key) + '=' + quote_rfc3986(value))
    return '&'.join(result)

def create_nonce():
    '''
    Generates ten hex encoded bytes of random data for use as an nonce
    '''
    data = os.urandom(10)
    return b16encode(data)

def create_signature(key, secret, user, email='', timestamp=None, nonce=None):
    '''
    Creates a signature for authenticating with Arkli
    '''
    if timestamp is None:
        timestamp = int(time.time())

    if nonce is None:
        nonce = create_nonce()

    parts = [
        ('arkli_email', email),
        ('arkli_key', key),
        ('arkli_nonce', nonce),
        ('arkli_timestamp', timestamp),
        ('arkli_user', user),
    ]
    basestr = urlencode_rfc3986(parts)
    h = hmac.new(secret, basestr, hashlib.sha1)
    signature = b64encode(h.digest())
    parts.append(('arkli_signature', signature))
    return parts

def create_signature_url(key, secret, user, email=''):
    parts = create_signature(key, secret, user, email)
    return urlencode_rfc3986(parts)
