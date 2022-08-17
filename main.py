# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Roger Hegstrom

Read the first two chapters in the text book.  This will get you acclimated to programming/ programming environment

Write a Python program to compute the sum of the first 100 integers.   In your GitHub account, open a repository 
called 'FirstProgram' Complete the assignment, push it up to your GitHub account, and turn in the GitHub URL for this problem


"""


cnt = 0 

for a in range(1, 101):
    cnt += a
    
print('The sum of the first 100 integers is: {}'.format(cnt))

