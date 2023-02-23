#!/usr/bin/env python3

from cmath import e


age=24
gender="male"
weight=75
height=180

if(age < 18) & (gender=="male"):
    if(weight > 90)|(height < 160):
        print("You are obese")
    else:
        print("You are healthy")
    



 