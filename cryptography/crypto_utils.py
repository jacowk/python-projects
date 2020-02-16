#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:52:55 2020

@author: jaco

Resource for this code:
https://nitratine.net/blog/post/encryption-and-decryption-in-python/
"""

import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

encrypted_file_name = 'system.encr'
decrypted_file_name = 'system.txt'

# Generate salt
#import os
#print(os.urandom(16))

def generate_salt():
    return os.urandom(16)

def generate_key():
    password_provided = get_password()
    password = password_provided.encode() # Convert to bytes
    salt = b'P\x1a\xe7m\xc8u\x10\xbf\xe8\xe2\xb1\xb8\xfff+\xc7' # Generated with os.urandom(16)
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    return key

def get_password():
    password_provided = input("Enter password: ")
    password_confirmation = input("Confirm password: ")
    while password_provided != password_confirmation:
        print("Passwords does not match. Please try again")
        password_provided = input("Enter password: ")
        password_confirmation = input("Confirm password: ")
    return password_provided


