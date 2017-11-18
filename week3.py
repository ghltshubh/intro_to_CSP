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

# Find words that are atleast as frequent as a given frequency
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result


# Counting total number of values(which can be a list) in a dictionary
def how_many(aDict):
    count = 0
    for values in aDict.values:
        count += len(values)
    return count

# Return key associated with the biggest value
def biggest(aDict):
    biggestValue = 0
    key = None
    for k, v in aDict.items():
        if len(v) >= biggestValue:
            key = k
            biggestValue = len(v)
    return key

# Test
biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []})


# Memoization
def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
print(fib_efficient(35,d))












