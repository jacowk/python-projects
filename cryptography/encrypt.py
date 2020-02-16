#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:37:45 2020

@author: jaco

Resource for this code:
https://nitratine.net/blog/post/encryption-and-decryption-in-python/

"""

from cryptography.fernet import Fernet
import crypto_utils
import os

# Generate a key and write it to file
'''key = Fernet.generate_key()
file = open('key.key', 'wb') # Stored as bytes
file.write(key)
file.close()
'''

# Read the key file
'''file = open('key.key', 'rb')
key = file.read()
key_decoded = key.decode() # Convert bytes to Python string
print(key_decoded)
'''

if os.path.exists(crypto_utils.decrypted_file_name):
    # Generate the key
    key = crypto_utils.generate_key()
    
    # Read clear text file
    clear_text_file = open(crypto_utils.decrypted_file_name, 'r')
    clear_text = clear_text_file.read()
    
    # Encrypt a string
    f = Fernet(key)
    encrypted = f.encrypt(clear_text.encode())
    
    # Write to file
    encrypted_file = open(crypto_utils.encrypted_file_name, 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()
    
    print("Encryption done")
    #if os.path.exists(crypto_utils.decrypted_file_name) and os.path.exists(crypto_utils.encrypted_file_name):
    #    os.remove(crypto_utils.decrypted_file_name)
else:
    print('File to encrypt does not exist')