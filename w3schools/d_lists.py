#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:18:34 2019

@author: jaco
"""
thislist = [ "apples", "bananas", "pears" ]
print(thislist)
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
    print(x)
    
if "apple" in thislist:
    print ("Apple is in the list")
    
print(len(thislist))
thislist.append("orange")
print(thislist)

thislist = [ "apple", "banana", "cherry" ]
thislist.insert(0, "orange")
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop();
print(thislist)

del thislist[0] # Remove a specified index
print(thislist)

thislist = [ "apple", "banana", "cherry" ]
del thislist # Delete the list completely
#print(thislist) Can't print thislist after del

thislist = [ "apple", "banana", "cherry" ]
thislist.clear() # Empties the list
print(thislist)

thislist = [ "apple", "banana", "cherry" ]
mylist = thislist.copy()
print(mylist)

thislist = [ "apple", "banana", "cherry" ]
mylist = list(thislist) # List constructor - Another way to create new list
print(mylist)

thislist = [ "apple", "banana", "cherry" ]
mylist = [ "pineapple", "pear", "strawberry" ]
list3 = thislist + mylist # Combine 2 lists
print(list3)

thislist = [ "a", "b", "c" ]
mylist = [ 1, 2, 3 ]
thislist.extend(mylist) # Another way to combine 2 lists
print(thislist)

mylist = list(("apple", "banana", "cherry"))
print(mylist)