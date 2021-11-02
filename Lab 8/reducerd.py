#!/usr/bin/python3

"""
Name - SHYAM MARJIT
Roll No - 1901195
Email - shyam.marjit@iiitg.ac.in
Assignment - 8
Part - D
"""

import sys

current_word = None
current_dict = {}

for line in sys.stdin:
    line = line.strip().split(',')
    word,line_num = line[0],int(line[1])

    if current_word == None:
        current_word = word
        current_dict[line_num] = 1
    elif current_word == word:
        if line_num in current_dict:
            current_dict[line_num] += 1
        else:
            current_dict[line_num] = 1
    else:
        #print(f'{current_word} : ',*sorted(current_dict.items()), sep=' ')
        print(f'{current_word} : {current_dict}')
        current_dict.clear()
        current_word = word
        current_dict[line_num] = 1

#print(f'{current_word} : ',*sorted(current_dict.items()), sep=' ')
print(f'{current_word} : {current_dict}')

