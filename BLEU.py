# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:35:54 2019

@author: Ranak Roy Chowdhury
"""
import sacrebleu

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
    
def computeBLEU(gold, generated):
    refs = [gold]
    sys = generated
    bleu = sacrebleu.corpus_bleu(sys, refs)
    return bleu.score

if __name__ == "__main__":
    print("Reading Files")
    gold_filename = 'gold_frozen.txt'
    generated_filename = 'generated_frozen.txt'
    gold, generated = readFiles(gold_filename, generated_filename)
    print('BLEU Score is: ' + str(computeBLEU(gold, generated)))