myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? ")
print(name)
colour = input("What is your favourite colour? ")
car = input("What is your favourite car? ")
print("{}, you like a {} {}".format(name,colour,car))