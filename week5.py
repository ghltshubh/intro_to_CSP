#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:56:54 2018

@author: shubhankar
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
print(paris_clock.time)
paris_clock.time = '10:30'
boston_clock.print_time()

X = 7
Y = 8
class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x              # won't work
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

w1 = Weird(X,Y)
print(w1.getX>())


class Animal(object):
    def __init__(self, age):
        self.age = age    # self.years = age hides internal representation
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return 'animal:'+str(self.name)+':'+str(self.age)

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'cat:'+str(self.name)+':'+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return 'rabbit:'+str(self.name)+':'+str(self.age)

class Person(Animal):
    def __init_(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, 'is', diff, 'years older than', other.name)
        else:
            print(self.name, 'is', diff, 'years younger than', other.name)
    def __str__(self):
        return 'person:'+str(self.name)+':'+str(self.age)

import random
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('i have homework')
        elif 0.25 <= r < 0.5:
            print('i should eat')
        elif 0.5 <= r < 0.74:
            print('i am watching tv')
    def __str__(self):
        return 'student:'+str(self.name)+':'+str(self.age)+':'+str(self.major)