#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 01:28:01 2017

@author: shubhankar
"""
# Avoid mutating a list as you are iterating over it, following program causes problem
#def remove_dups_erroneous(L1, L2):
#    for e in L1:           # looping while mutating
#        if e in L2:
#            L1.remove(e)
            

# Correct way of doing this
def remove_dups(L1, L2):
    L1_copy = L1[:]      # Create a copy 
    for e in L1_copy:
        if e in L2:
            L1.remove(e)


            
# Lyrics to frequency
def lyrics_to_frequency(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# Find the most common words
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
























