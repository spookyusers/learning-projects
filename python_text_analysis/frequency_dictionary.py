#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:44:56 2024

@author: kym
"""

reader = open('/home/kym/books/jekyll_and_hyde.txt')

frequency_dict = {}

for line in reader:
    for word in line.split():
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
print(frequency_dict["Dr."])
