# Advanced data types

# Mutable vs Immutable

# Mutable- data types that can be edited during program life cycle
# add/remove elements 
# Immutable- data types that cannot be edited during program life cycle

# 1.List (mutable)

friends = ["Marvin","Alex","Anna"]
# or friends = [] for an empty list
# add
students = ["Jane","Ali","Sammy"]

friends.extend(students)
friends.append("Joseph")

# 2.Tuples (immutbale)
# Type of list that are immutable

stationeries = ("pens","books","erasers","pencils")

# replace the whole list 

stationeries = ("rulers","clipboards","staplers")

for stationery in stationeries:
    print(stationeries)

numbers = (1,2,3,4,5)

# 3.Dictionaries aka dict
# - uses key and value pair

student = {"Name": "Adrian","Age": 18,"Gender":"Male","is tall":False}
print(student["Name"])
print(student["Age"])
print(student["Gender"])
print(student["is tall"])

print(student.values())
print(student.keys())

# "name": "Adrian"--> name(key) Adrian(value)

friend = {"Favourite_colour": "Black","Hobby":"Swimming","Course":"Psychology","Weight":"75 Kg","Height":"175 cm"}
print(friend["Favourite_colour"])
print(friend["Hobby"])
print(friend["Course"])
print(friend["Weight"])
print(friend["Height"])

# 4.Sets