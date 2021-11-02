#!/usr/bin/env python3

"""
Name - SHYAM MARJIT
Roll No - 1901195
Email - shyam.marjit@iiitg.ac.in
Assignment - 8
Part - B and C
"""

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip().split(',')
    word,count = line[0],int(line[1])

    if current_word == None:
        current_word = word
        current_count = count
    elif current_word == word:
        current_count += count
    else:
        print(f'{current_word},{current_count}')
        current_word = word
        current_count = count

print(f'{current_word},{current_count}')
