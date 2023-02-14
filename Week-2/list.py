#Typing a list

names=["Adrian","Elton","Denise","Florence","Henry"]

print(names)

print(names[0:3])

print(names[2])

fruits=["Bananas","Apples","Mangoes","Watermelons"]

print(fruits[0:-1])

print("My favourite fruit is:",fruits[2].upper())

vegetables=("Cabbages","Onions","Spinach","Broccoli")

stationery=("Pens","Pencils","Erasers","Books","Rulers")

shoppings = vegetables + stationery 

print(shoppings)

print(shoppings[5])

for vegetable in vegetables: 
  print(vegetable)

for shopping in shoppings:
  print(shopping)

  print("My name is", names[0] + " "   "and my favourite fruit is", fruits[3])