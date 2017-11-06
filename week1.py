# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:52:15 2016

@author: shubhankar
"""
    
x = input("Input number to be squared: ")
ans = 0
itersLeft = int(x)
while itersLeft != 0:
    ans += int(x)
    itersLeft -= 1
print(x + " squared is: " + str(ans))

# count vowels
s = "ihqowefowiehufjhwfiapoe"
numOfVowels = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or \
    letter == "u":
        numOfVowels += 1
print("Number of vowels: " + str(numOfVowels))

# Number of times the string 'bob' occurs in s. 
s = 'boobbobbobaobobbob'
count = 0
for i in range(len(s)):
        if i < len(s) - 2 and s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count += 1
            i += 2
print('Number of times bob occurs is: %d' %(count))


# longest substring in alphabatical order
s = 'azcbobobegghakl'
currentSubstring = s[0]
maxSubstring = s[0]
for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        currentSubstring += s[i+1]
        if len(currentSubstring) > len(maxSubstring):
            maxSubstring = currentSubstring
    else:
        currentSubstring = s[i+1]
print("Longest substring in alphabhatical order is: ", maxSubstring)



# return indices of contiguous substring of intList whose contituents sum clsest to n
intList = [1,4,2,6,5,9]
n = 13
def closest_substring(intList, n):
    closest = {}
    for i in range(len(intList)):
        sum = 0
        for j in range(i, len(intList)):
            sum += intList[j]
            closest.update({(i,j):abs(sum - n)})
    closest = sorted(closest.items(), key=lambda x:x[1])
    return closest[0][0]

# find integral point inside or on a triangle whose sum of distances from each 
# vertex is minimum
def area(x1,y1,x2,y2,x3,y3):
    a = ((x1-x2)**2 + (y1-y2)**2)**0.5
    b = ((x2-x3)**2 + (y2-y3)**2)**0.5
    c = ((x3-x1)**2 + (y3-y1)**2)**0.5
    S = (a+b+c)/2
    A = (S*abs(S-a)*abs(S-b)*abs(S-c))**0.5
    return A
def minimum_sum(x1, y1, x2, y2, x3, y3):
    distSum = {}
    for x in range(min(round(x1),round(x2),round(x3)), 
                   max(round(x1),round(x2),round(x3))+1):
        for y in range(min(round(y1),round(y2),round(y3)), 
                       max(round(y1),round(y2),round(y3))+1):
            try:
                if round(area(x,y,x2,y2,x3,y3) + area(x1,y1,x,y,x3,y3) + 
                         area(x1,y1,x2,y2,x,y),4) == round(area(x1,y1,x2,y2,x3,y3),4):
                    dist = ((x-x1)**2 + (y-y1)**2)**0.5 + ((x-x2)**2 + 
                            (y-y2)**2)**0.5 + ((x-x3)**2 + (y-y3)**2)**0.5
                    distSum.update({(x,y):dist})
            except:
                print("x: %f y:%f" %(x,y))   
                print(area(x,y,x2,y2,x3,y3), area(x1,y1,x,y,x3,y3), \
                      area(x1,y1,x2,y2,x,y))
    distSum = sorted(distSum.items(), key=lambda x:x[1])
    if len(distSum) > 0:
        return [i for i in distSum[0][0]]
    else:
        return [None, None]

