#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:35:59 2020

@author: jaco

https://developers.google.com/gmail/api/quickstart/python

"""
#help("modules")

from __future__ import print_function
import gmail_oo.gmail_connector as gc
import gmail_oo.label_printer as lp

class QuickStartApp:

    def run(self):
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        label_printer = lp.LabelPrinter(service)
        label_printer.print()

if __name__ == '__main__':
    quick_start_app = QuickStartApp()
    quick_start_app.run()
