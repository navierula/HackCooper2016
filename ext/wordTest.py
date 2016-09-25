# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:16:45 2016

@author: navrajnarula
"""

import nltk
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
    #neg = ascii(neg)
    neg = open(neg_words, "r")
    # tokenize each word in file
    text = []
    #neg = ascii(neg)
   # print(neg)
    for line in neg:
        #line = ascii(line)
        # avoid issues with ASCII
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
        
    pos_Sum = sum(posWords.values())
    neg_Sum = sum(negWords.values())
    neutral_Sum = sum(neutralWords.values())
    
    sumAll = pos_Sum + abs(neg_Sum) + neutral_Sum
    posNum = pos_Sum / sumAll
    negNum = abs(neg_Sum) /sumAll
    neutralNum = neutral_Sum / sumAll 
    
    return (posNum, negNum)
    
nums = calcSentiment(wordList, pos, neg)
    
def result(nums):
    if nums[1] >= 30:
        print("Your comments are mostly negative", round(nums[1] * 100,2), "percent, to be exact. Consider lightening your tone.")
    else:
        print("Your comments are", round(nums[1] * 100,2), "negative. Not too bad!")
        if nums[0] >= 40:
            print("In fact, there're extremely uplifting!")
        

                
                
                
                
         


        
        
        
        

            

                
                
                
            