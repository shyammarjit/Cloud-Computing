#!/usr/bin/env python3

"""
Name - SHYAM MARJIT
Roll No - 1901195
Email - shyam.marjit@iiitg.ac.in
Assignment - 8
Part - A
"""

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    line = re.sub('[^A-Za-z0-9\s]+', '', line)
    words = line.split()
    for word in words:
        print(word)
