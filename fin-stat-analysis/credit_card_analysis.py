#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:18:05 2020

@author: jaco

Read the CSV file

Generate a JSON file for the given month's credit card statement

Write the JSON to date stamped file

Calculate total per transaction types
Calculate total income
Calculate total expenses

Generate a JSON for the final statement

Write the JSON report to file. JSON output:
{
     "period": 2019-11
     "total-income": 0,
     "total-expenses": 0,
     "profit-loss": 0,
     "income-transactions": [
        "xxxxxxxx": {
            "total": 0,
            "no-of-transactions" : 0
        },
        "xxxxxxxx": {
            "total": 0,
            "no-of-transactions" : 0
        }
     ],
     "expense-transactions": [
        "xxxxxxxx": {
            "total": 0,
            "no-of-transactions" : 0
        },
        "xxxxxxxx": {
            "total": 0,
            "no-of-transactions" : 0
        }
     ]
}
"""
import pandas as pd
import json
import os
from datetime import datetime
from shutil import copyfile

# Before starting, copy the CSV file to this directory
current_date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
date = "202007"
input_filename = "CreditCardTransactionHistory" + date
base_path = "/home/jaco/python-data/fin-stat-analysis"
account_type = "CreditCard"
output_path = os.path.join(base_path, account_type, date)
prepare_directory(output_path)

input_copy_filename = "{}.csv".format(input_filename)
input_copy_filename_path = os.path.join(base_path, output_path, input_copy_filename)

copyfile("{}.csv".format(input_filename), input_copy_filename_path)

transaction_filename = "{}TransactionHistory{}.json".format(account_type, date)
transaction_path = os.path.join(base_path, output_path, transaction_filename)

summary_filename = "{}TransactionSummary{}.json".format(account_type, date)
summary_path = os.path.join(base_path, output_path, summary_filename)

summary = {"date stamp": current_date_time, "period": date}

# Read the CSV file
csv_file = pd.read_csv("{}.csv".format(input_filename))

# Generate a JSON file from the CSV
transaction_data = []
for index, row in csv_file.iterrows():
    json_row = { 
                'Date': row['Date'], 
                'Description': row['Description'],
                'Amount': row['Amount'],
                }
    transaction_data.append(json_row)

final_data = { 'transactions' : transaction_data }
json_file = json.dumps(final_data, indent=1)

# Write the JSON file
output_file = open(transaction_path, 'w')
output_file.write(json_file)
output_file.close()

# Calculate total income
total_income = 0
for transaction_dict in transaction_data:
    amount = transaction_dict['Amount']
    if amount > 0:
        total_income += amount
        #print(transaction_dict)

summary['total_income'] = total_income
print('Total income: ' + str(total_income))

# Calculate total expenses
total_expenses = 0
for transaction_dict in transaction_data:
    amount = transaction_dict['Amount']
    if amount < 0:
        total_expenses += amount
        #print(transaction_dict)
    
summary['total_expenses'] = total_expenses
print('Total expenses: ' + str(total_expenses))

# Calculate profit/loss
profit_loss = total_expenses + total_income 
summary['profit_loss'] = profit_loss
print('Profit/Lost: ' + str(profit_loss))

# Calculate total expenses per transaction type
income_transactions_list = []
expense_transactions_list = []
for expense_transaction_type in expense_transaction_types:
    # Initialize variables per transaction type
    total = 0
    no_of_transactions = 0
    total_type_expenses_dict = {}
    for transaction_dict in transaction_data:
        if expense_transaction_type in transaction_dict['Description']:
            if transaction_dict['Amount'] < 0:
                total += abs(transaction_dict['Amount'])
                no_of_transactions += 1
    
    total_type_expenses_dict[expense_transaction_type] = {
        "total": total, 
        "no_of_transactions": no_of_transactions
    }
    expense_transactions_list.append(total_type_expenses_dict)

summary['expense_transactions'] = expense_transactions_list

# Calculate total income per transaction type
income_transactions_list = []
for income_transaction_type in income_transaction_types:
    total = 0
    no_of_transactions = 0
    total_type_income_dict = {}
    for transaction_dict in transaction_data:
        if income_transaction_type in transaction_dict['Description']:
            if transaction_dict['Amount'] > 0:
                total += abs(transaction_dict['Amount'])
                no_of_transactions += 1
    
    total_type_income_dict[income_transaction_type] = {
        "total": total, 
        "no_of_transactions": no_of_transactions
    }
    income_transactions_list.append(total_type_income_dict)

summary['income_transactions'] = income_transactions_list

# Determine unknown transactions
unkown_transactions_list = []
for transaction_dict in transaction_data:
    unknown_transaction_dict = {}
    unknown = True
    for income_transaction_type in income_transaction_types:
        if income_transaction_type in transaction_dict['Description']:
            unknown = False
    
    for expense_transaction_type in expense_transaction_types:
        if expense_transaction_type in transaction_dict['Description']:
            unknown = False
    
    if unknown:
        unknown_transaction_dict = {
            "date": transaction_dict['Date'],
            "description" : transaction_dict['Description'],
            "amount": transaction_dict['Amount']
        }
        unkown_transactions_list.append(unknown_transaction_dict)
summary['unknown_transactions'] = unkown_transactions_list
        
json_file = json.dumps(summary, indent=1)

# Write the JSON file
output_file = open(summary_path, 'w')
output_file.write(json_file)
output_file.close()
