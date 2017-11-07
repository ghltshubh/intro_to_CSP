#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:52:15 2017

@author: shubhankar
"""


# square root
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
    
    
    
# guess the number
print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high)//2
print("Is your secret number " + str(ans))
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
              the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while guess != 'c':
    if guess == 'h':
        high = ans
        ans = (low + high)//2
        print("Is your secret number " + str(ans))
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to \
                      indicate the guess is too low. Enter 'c' to indicate I \
                      guessed correctly. ")
    elif guess == 'l':
        low = ans
        ans = (low + high)//2
        print("Is your secret number " + str(ans))
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' \
                      to indicate the guess is too low. Enter 'c' to indicate \
                      I guessed correctly. ")
    else: 
        print("Invalid input")
        print("Is your secret number " + str(ans))
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' \
                      to indicate the guess is too low. Enter 'c' to indicate \
                      I guessed correctly. ")
        
print("Game over. Your secret number was: " + str(ans))



# decimal to binary
isNeg = False
num = int(input("Input an integer to be converted to binary: "))
numbr = num
if num < 0:
    isNeg = True
    num = abs(num)
binary = ''
if num == 0:
    binary = '0'
while num != 0:          
    binary = str(num%2) + binary   
    num = num//2  
if isNeg:
    binary = '-' + binary
print(str(numbr) + " in binary is " + binary)


# decimal fraction to binary fraction
x = float(input("Enter a decimal number between 0 and 1: "))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

binary = ''
if num == 0:
    binary = '0'
while num > 0:          
    binary = str(num%2) + binary   
    num = num//2

for i in range(p - len(binary)):
    binary = '0' + binary
    
binary = binary[0:-p] + '.' + binary[-p:]
print('The binary representation of the decimal ' + str(x) + ' is\n' + binary)


'''
#newton-raphson method#
for any approximate root of the polynomial of type f(x) = x^a - b,
a better approximation would be 
    g - f(g)/f'(g)
where g is an approximate root of f(x)
'''

# square root using newton-raphson
# a = 2
num = int(input("Enter a number whose squar root is to be computed: "))
epsilon = 0.0000001
guess = num/2.0
numGuesses = 0

while abs(guess*guess - num) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - num)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(num) + ' is about ' + str(guess))

# String manipulation
a = 'number one - the larch'
a.capitalize()   # Capitalizes the first letter
a.upper()        # Capitalizes the whole string
a.isupper()
a.islower()
a = a.capitalize()
a.swapcase()
a.index('e')     # index of first 'e', returns an error if not found
a.find('e')      # index of 'e', returns -1 if not found
a.count('e')
a.replace('one', 'seven')


# recursive exponent
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        result = 1
    else:
        exp -= 1
        result = base*recurPower(base, exp)

    return result

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)







