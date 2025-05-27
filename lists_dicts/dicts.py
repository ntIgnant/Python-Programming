myDict = {1: "Hassan", 2: "Ignacio", 3: "Oscar", 4: "Sarah", 5: "Alexa"}

names = [val for key, val in myDict.items()] # create a list with the names using list comprehension
keys = [key for key, val in myDict.items()] # create a list with the keys of the dict

print(names, keys)

for k, v in myDict.items():
    print(k, v)