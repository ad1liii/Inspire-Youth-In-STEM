#!/usr/bin/env python3

#This is a single line comment
#Python program to illustrate the use of operators
#Name: Adrian Wambuma
#Email: awambuma@gmail.com
#Date: 17th Feb,2023
#File: operators.py

poem= """This is a poem about nothing
        Its funny people laugh about nothing"""

print(poem)
print(len(poem))

f_name= "Adrian"
s_name= "Wambuma"

full_name= f_name + " " + s_name

age= 18
print("My name is ", full_name + " " "and I am ", str(age)+ " "  "years old.")

print("My name is {} and I am {} years old".format(full_name,age))

print("Hello Adrian. \n How are you? \n I am fine.")
print("Hello Adrian. \t How are you? \t I am fine.")
