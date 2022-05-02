thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    'colors': ['red', 'white', 'blue']
}
# get values
print(thisDict['brand'], thisDict.get('model'))
print(thisDict)
print(f"dictionary length: {len(thisDict)}")

# get items, keys, values
print(f'items : {thisDict.items()}')
print(f'keys : {thisDict.keys()}')
print(f'values : {thisDict.values()}')

# check if key exists
if 'model' in thisDict:
    print(thisDict['model'])

# update values
thisDict.update({'year': 1990})
print(thisDict)

# Remove items
thisDict.pop('model')
print(f'removed item "model" using pop {thisDict}')
thisDict.popitem()
print(f'removed last item "colors" using popitem {thisDict}')
del thisDict['brand']
thisDict.update({'model': 'Honda'})
# thisDict.clear()

# loop through the dictionaries
thisDict.update({"brand": "Ford"})
for item in thisDict.items():
    print(item)
for key in thisDict.keys():
    print(f'key : {key}')
for value in thisDict.values():
    print(f'value : {value}')

# copy, create dictionary
newDict1 = dict(thisDict)
newDict2 = newDict1.copy()
print(f'copied using  "dict" : {newDict1}')
print(f'copied using "copy" method : {newDict2}')

family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(f'New dictionary : {family}')

# find the letter occurrence in sentence
sentence = "Find the each letter occurrence"
valuesOccurrences = {}
for char in sentence:
    if char in valuesOccurrences:
        valuesOccurrences[char] += 1
    else:
        valuesOccurrences[char] = 1

print(valuesOccurrences.items())
sortedOccurrences = sorted(valuesOccurrences.items(), key=lambda character: character[1], reverse=True)
print(f'sorted occurrences : {sortedOccurrences}')
print(f'High Occurred char is : {sortedOccurrences[0]}')
