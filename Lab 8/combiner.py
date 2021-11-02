#!/usr/bin/env python3

"""
Name - SHYAM MARJIT
Email - shyam.marjit@iiitg.ac.in
Roll No - 1901195
Part - C
"""

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip().split(',')
    word,count = line[0],int(line[1])

    if current_word == None:
        current_word = word
        current_count = 1
    elif current_word == word:
        current_count += 1
    else:
        print(current_word + "," + str(current_count))
        current_word = word
        current_count = 1

print(current_word + "," + str(current_count))
