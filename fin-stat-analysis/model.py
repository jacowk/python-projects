#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:53:38 2020

@author: jaco
"""
import os

income_transaction_types = [
'DIRECT CREDIT DISC',
'LFCC CAMERA'
]

expense_transaction_types = [
'ABSA LIFE',
'MONITOR24',
'TRANSACTION CHARGE',
'CARTRACK',
'INTERNET BANK FEE',
'ABSAHLOAN',
'FORMEALS',
'MWBSA',
'AFRIFORUM',
'OMSUREPREM',
'DISC INVT',
'DISCLIFE',
'ADMINISTRATION FEE',
'INETBNK PAY DEBIT',
'INETBNK TRF DEBIT',
'MTN SP',
'ATM WITHDRAWAL',
'NOTIFICATION FEE',
'HH FONDS'
]

def prepare_directory(output_path):
    if (not os.path.exists(output_path)):
        os.makedirs(output_path)
    
    
    