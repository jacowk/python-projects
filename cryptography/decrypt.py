#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:08:40 2020

@author: jaco

Resource for this code:
https://nitratine.net/blog/post/encryption-and-decryption-in-python/
"""

from cryptography.fernet import Fernet
import crypto_utils
import os

# Generate the key
key = crypto_utils.generate_key()

# Read file
if os.path.exists(crypto_utils.encrypted_file_name):
    encrypted_file = open(crypto_utils.encrypted_file_name, 'rb')
    encrypted_data = encrypted_file.read()
    encrypted_file.close()
    
    # Decrypt
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    
    # Write decrypted data to file
    decrypted_file = open(crypto_utils.decrypted_file_name, 'w')
    decrypted_file.write(decrypted_data)
    decrypted_file.close()
    
    print("Decryption done")
    
    #os.remove(crypto_utils.encrypted_file_name)
else:
    print('File to decrypt does not exist')