#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:06:20 2024
Word frequency counter
@author: kym
"""

from collections import Counter


reader = open('/path/filename.txt')

# create a Counter object called counter
word_counts = Counter()

for line in reader:
  for word in line.split():
    clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
    word_counts[word] += 1
 
print(word_counts.most_common(5))     
#print(counter['hyde'])