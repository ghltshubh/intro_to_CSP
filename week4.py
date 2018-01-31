#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:12:58 2018

@author: shubhankar
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    myDict = {}
    L = []
    for k, v in aDict.items():
        if v in myDict:
            myDict[v] += 1
        else:
            myDict[v] = 1

    for k, v in myDict.items():
        if v == 1:
            for i, j in aDict.items():
                if j == k:
                    L.append(i)
    return sorted(L)


def general_poly(L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def inner(x):
        res = 0
        n = len(L)-1
        for e in range(len(L)):
            res += L[e]*x**n
            n -= 1
        return res
    return inner

data = []
file_name = input("Provide a name of a file of data: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
    fh.close()

gradesData = []
if data:
    for student in data:
        try:
            name = student[:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[:], []])


def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")












