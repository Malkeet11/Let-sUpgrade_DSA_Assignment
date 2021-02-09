'''
Python-Handler
Author : Malkeet Singh
Assignment - 3
Date : 2021-02-06

Write a Python program to print even numbers in a list.
Sample:
Input: list1 = [12, 3, 55, 6, 144]
Output: [12, 6, 144]
Input: list2 = [2, 10, 9, 37]
Output: [2, 10]

'''

# Taking User Input Base in List l
l = [int(i) for i in input().split()]

# Finding Even Numbers in List l and Storing Output List l
o = [i for i in l if not(i & 1)]

# Print/Display Output List o
print(o)
