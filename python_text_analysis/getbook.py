#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:18:01 2024
Download Open-source Material
@author: kym
"""

import requests

# URL for "The Strange Case of Dr. Jekyll and Mr. Hyde"
url = 'https://www.gutenberg.org/files/42/42-0.txt'
response = requests.get(url)

if response.status_code == 200:
    with open('/home/kym/books/jekyll_and_hyde.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    text = response.text
    print(text[:1000]) # Print a preview
else:
    print("Failed to retrieve the book.")

