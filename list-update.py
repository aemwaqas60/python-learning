myList = ['apple', 'banana', 'orange', 'guwa']
list1 = ['kiwi', 'papaya']
print('Original List: ', myList)

# Insert range of items
# If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:
myList[1:2] = ['mango', 'Watermelon', 'pineapple']
print(' More Item than Range: ', myList)
# If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:

myList[1:3] = ['cherry']

print(' Less Item than Range: ', myList)

print('---- append, insert method -----')
myList.append('blue-berry')
myList.insert(4, 'red-berry')
print(myList)

# Extend the list
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
print('----- Extend the list -----')
myList.extend(list1)

print('Extended List: ', myList)
tupleName = ('Waqas', 'Jhon', 'Mark')
myList.extend(tupleName)
print('Extneded list using tuple: ', myList)

# Remove the list items
# If you do not specify the index, the pop() method removes the last item.
print('------ Remove list items ------')
myList.pop(1)
print('remove list item using pop at index 1 : ', myList)
myList.pop()
print('remove list item using pop at the end : ', myList)
del myList[2]
print('remove list item at index 2 using del : ', myList)
myList.clear()
print('Clear the list: ', myList)
