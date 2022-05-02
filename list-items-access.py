myList = ['apple', 'banana', 'cherry', 'orange', 'blue-berry']

# Negative indexing, means start from end
print(myList[-1], myList[-2])

# ===== Range of indexes ======
# By leaving out start value, the range will start at first item
# By leaving out end value, the range will end on last item
print('----- Range of Indexes -----')
print(myList[0:2])
print(myList[: 3])
print(myList[0:])

# Range negative indexes
print('----- Range of Negative Indexes -----')
print(myList[-4: -1])

# Check if item exists
print('---- check if item exists -----')
if 'apple' in myList:
    print('Yes, the apple in the fruit list')