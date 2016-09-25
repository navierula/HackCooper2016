# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:16:45 2016

@author: navrajnarula
"""

import nltk
import sys
from collections import defaultdict

filename = "yellowWall.txt"
# files retrieved from Bing Liu's opinion lexicon
pos_words = "pos-words.txt"
neg_words ="neg-words.txt"

def readFile(filename):
    # open file
    filename = open(filename, "r")
    # tokenize each word in file
    text = []
    for line in filename:
        # avoid issues with ASCII
        #line = line.decode("utf-8")
        if len(line) > 1:
            line.rstrip('\n').split()
            text.append(nltk.word_tokenize(line))
    return text
    
tokenizeSentences = readFile(filename)

def printTokens(tokenizeSentences):
    wordList = []
    for line in tokenizeSentences:
        # print each individual word in the file
        for item in line:
            if len(item) > 2:
                wordList.append(item)
    return wordList
    
wordList = printTokens(tokenizeSentences)

def positive(wordList, pos_words):
    pos = open(pos_words, "r")
    # tokenize each word in file
    text = []
    for line in pos:
        # avoid issues with ASCII
        #line = line.decode("utf-8")
        if len(line) > 1:
            line.rstrip('\n').split()
            text.append(nltk.word_tokenize(line))
    wordList = []
    for line in text:
        # print each individual word in the file
        for item in line:
            if len(item) > 2:
                wordList.append(item)
    return wordList
    
def negative(wordList, neg_words):
    pos = open(pos_words, "r")
    # tokenize each word in file
    text = []
    for line in pos:
        # avoid issues with ASCII
        #line = line.decode("utf-8")
        if len(line) > 1:
            line.rstrip('\n').split()
            text.append(nltk.word_tokenize(line))
    wordList = []
    for line in text:
        # print each individual word in the file
        for item in line:
            if len(item) > 2:
                wordList.append(item)
    return wordList
    
pos = positive(wordList, pos_words)
neg = negative(wordList, neg_words)
        
def calcSentiment(wordList, pos, neg):
    posWords = defaultdict(float)
    negWords = defaultdict(float)
    neutralWords = defaultdict(float)
    for item in wordList:
        if item in pos:
            if not item in posWords:
                posWords[item] = 1
            else:
                posWords[item] += 1
        elif item in neg:
            if not item in negWords:
                negWords[item] = -1
            else:
                negWords[item] -= 1
        else:
            if not item in neutralWords:
                neutralWords[item] = 0
            else:
                neutralWords[item] += 1
    
    
                
                
                
                
         


        
        
        
        

            

                
                
                
            