# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:42:07 2019

@author: Ranak Roy Chowdhury
"""

from SpiceClass import Spice

def readFiles(gold_filename, generated_filename):
    f = open(gold_filename)
    gold = []
    for line in f:
        gold.append(line)
    f = open(generated_filename)
    generated = []
    for line in f:
        generated.append(line)
    return gold, generated
    
def computeSPICE(gold, generated):
    spice = Spice()
    score = spice.compute_score(gold, generated)
    print(score)

if __name__ == "__main__":
    print("Reading Files")
    gold_filename = 'gold_frozen.txt'
    generated_filename = 'generated_frozen.txt'
    gold, generated = readFiles(gold_filename, generated_filename)
    computeSPICE(gold, generated)
    #print('SPICE Score is: ' + str(computeSPICE(gold, generated)))