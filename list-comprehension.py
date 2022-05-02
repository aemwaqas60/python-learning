list1 = ['apple', 'banana', 'cherry', 'kiwi']
products = [('product1', 100), ('product2', 150), ('product3', 200)]

print('Original list : ', list1)
print('--- create a new list, with condition of list item contains a letter')
newList = [item for item in list1 if 'a' in item]
print('New list: ', newList)

print('--- create a new list, with condition of list item is not equal is "apple"')
newList = [item for item in list1 if item != 'apple']
print('New list: ', newList)
print('--- create a new list, with condition of list item < 5 "')
list2 = list(range(10))
print('Original list : ', list2)
newList = [item for item in list2 if item < 5]
print("New list : ", newList)

print('--- Return "orange" instead of "banana" with upper case ---- ')
print('New list: ', [item.upper() if item != 'banana' else 'orange'.upper() for item in list1])

# mapping, filtering using list comprehension
mappedList = [product[1] for product in products]
print('mapping products: ', mappedList)

filteredList = [product for product in products if product[1] > 100]
print('filtered products: ', filteredList)
