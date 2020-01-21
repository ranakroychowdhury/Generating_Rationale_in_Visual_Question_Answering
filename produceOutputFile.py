# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:29:21 2019

@author: Ranak Roy Chowdhury
"""

def readFiles(filename):
    f = open(filename, encoding="utf8")
    lines = f.readlines()
    imp_lines = []
    for line in lines:
        if 'Gold' in line and 'Generated' in line:
            imp_lines.append(line)
    gold = []
    generated = []
    for line in imp_lines:
        a = line.split('|')
        for substring in a:
            if 'Gold rationale:' in substring:
                string = substring.replace(' Gold rationale: ', '')
                string = string.replace('.', '')
                gold.append(string)
            elif 'Generated rationale:' in substring:
                string = substring.replace(' Generated rationale: ', '')
                string = string.replace('.', '')
                generated.append(string)
    return gold, generated

def writeFiles(gold_filename, generated_filename, gold, generated):
    with open(gold_filename, 'w', encoding='utf-8') as f:
        for item in gold:
            f.write("%s\n" % item)
    with open(generated_filename, 'w', encoding='utf-8') as f:
        for item in generated:
            f.write("%s" % item)
            
if __name__ == "__main__":
    print("Reading Files")
    filename = 'vilbert_frozen_ep20.txt'
    gold, generated = readFiles(filename)
    gold_filename = 'gold_frozen.txt'
    generated_filename = 'generated_frozen.txt'
    writeFiles(gold_filename, generated_filename, gold, generated)