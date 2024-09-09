# ✅ Functions
import math


# 1. Built In.py - Created by Python Guys
# input()
# print()
# max()
# type()
# id()
# pow()
# len()
# list()
# math.cos()
# range()
# math.factorial()
# sorted()
# int()
# str()
# #random()
# float()
# bool()
# str.lower()
# str.upper()


# 2. Custom created, User Defined
# definition
def greet():
    print("Hello, there!!")


# calling
greet()


# Types of Functions in Python
# 1. Built-in functions - len(), min(), and print() are examples of built-in functions.
# https://docs.python.org/3/library/functions.html#built-in-funcs
# 2. User-defined functions


# def and call
# user definded functions

def greet_to_all_of_you():
    print("Hello, Everyone")


def greet():
    print("Yes")


greet()
greet_to_all_of_you()



# def and call
# user definded functions

def greet_to_all_of_you():
    print("Hello, Everyone")

# .lower() - string
def greet():
    print("Yes")
    greet_to_all_of_you()

greet_to_all_of_you()


# functions with argument, parameters

def greet():
    print("Hello, there!!")


def greet_by_name(pramod): # name -> variable name, argument | parameter
    print("Hello,", pramod)

greet_by_name("Pramod")
greet_by_name(123)
greet_by_name(True)
greet_by_name(3.14)


# functions with user input

def greet(name):
    print("Hello,", name)


name = input("Enter your name\n")
greet(name)
