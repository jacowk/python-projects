#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:53:38 2020

@author: jaco
"""
import os

income_transaction_types = [
'From savings'
]

expense_transaction_types = [
'CHECKERS ROCK COTTAGE',
'ABSA RL',
'MAANDELIKSE REKENINGFOOI',
'KREDIETFASILITEIT-DIENSFOOI',
'KREDIET LEWENS PREMIE',
'AMZN Digital',
'NETFLIX.COM',
'RENTE BETAAL',
'ROCK COTTAGE PHARMACY',
'SEATTLE DISCOVERY',
'SPAR RETCROSSING',
'TOTAL RA ROCK COTTAGE',
'Radiokop Spar',
'COMPASS GROUP SA',
'CNA CORP DISCOVERY',
'WEST PACK LIFE STYLE',
'Clicks Discovery place',
'CALTEX TOM JONES',
'SASOL WILROPARK',
'WOOLWORTHS DISCOVERY'
]

def prepare_directory(output_path):
    if (not os.path.exists(output_path)):
        os.makedirs(output_path)
    
    
    