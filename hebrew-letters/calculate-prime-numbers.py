#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:09:19 2020

@author: jaco
"""

# Python program to display all the prime numbers within an interval

lower = 0
upper = 1000000
max_no = 101
prime_numbers = []

print("Prime numbers between", lower, "and", upper, "are:")
cnt = 1
for num in range(lower, upper + 1):
   if cnt == max_no:
        break
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print("{} - {},".format(str(cnt), str(num)))
           cnt += 1
           prime_numbers.append(num)

print(prime_numbers)