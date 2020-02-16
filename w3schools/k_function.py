#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:25:08 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_functions.asp

# Basic function
def my_function():
    print("Hello from a function")
    
my_function()

# Arguments
def my_function(fname): 
    print(fname + " Refsnes")
    
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arguments
def my_function(fname, sname): #parameters
    print(fname + sname)
    
my_function("Emil", " Refsnes") #arguments
my_function("Tobias", " Refsnes")
my_function("Linus", " Refsnes")

# Arbitrary arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword arguments - The order doesn't matter
# called kwargs in Python documentation
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary keyword arguments
# Shortened to **kwargs in Python documentation
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Default parameter
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list as an argument
def my_function(food):
    for x in food:
        print(x)

fruits = [ "apple", "banana", "cherry" ]
my_function(fruits)

# Return values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement
# A function definition cannot be empty. Used if your function for some reason
# has no content
def my_function():
    pass

my_function()

# Recursion
# When a function has to call itself
def my_function(x):
    print(x)
    if x == 3:
        return
    else:
        x += 1
        my_function(x)

my_function(0)






