#!/usr/bin/env python3

MyFavouriteFruits= ["watermelons","oranges","bananas","apples","mangoes"]

for MyFavouriteFruit in MyFavouriteFruits:
    print(MyFavouriteFruits)

print(len(MyFavouriteFruits))

#len prints the number of elements in the list

Friends=["Ken","Sammy","Sandra","Mark","Samantha"]

print(Friends)

Friends[0] = "Sandra"

print(Friends)

#append()- adds an element at the end
#clear()-removes all the
#copy()- returns the number
#insert()-adds an element at the specified position
#pop()- removes the element
#count()- returns the number
#sort()-sorts


new_friends=[Friends.copy()]
print(new_friends)

new_friends.sort()

print(new_friends)

new_friends.pop()

print(new_friends)

new_friends