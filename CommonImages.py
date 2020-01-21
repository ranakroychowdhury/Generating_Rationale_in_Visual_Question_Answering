# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:45:20 2019

@author: Ranak Roy Chowdhury
"""

def readFiles(file):
    f = open(file, encoding="utf8")
    lines = f.readlines()
    frozen = set()
    for line in lines:
        if 'Img ID: ' in line:
            words = line.split()
            idx = words.index('ID:')
            s = words[idx + 1].replace(']', '')
            frozen.add(int(s))
    print(frozen)
            
            
    
    
if __name__ == "__main__":
    print("Reading Files")
    file1 = 'vilbert_frozen_ep20.txt'
    file2 = 'vilbert-gpt2-ep10.log'
    readFiles(file2)