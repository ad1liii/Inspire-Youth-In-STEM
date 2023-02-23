#!/usr/bin/env python3

age= 16

gender= "Male"

if(age < 18):
    print("You are still young")
else:
    print("You should get an ID")

#Compound/multiple conditions

if((age>30) & (gender=="Male")):
    print("You qualify for a loan")   
else:
    print("No loan for you")

fav_colour= "gray"
age= 22

if(fav_colour== "gray") | (age<=20):
    print("Happy birthday")
else:
    print("No birthday present for you yet")

