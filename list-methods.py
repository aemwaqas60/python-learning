from builtins import list

list1 = [100, 50, 65, 82, 23]
list2 = ["orange", "mango", "kiwi", "pineapple", "banana"]

products = [('product1', 100), ('product2', 150), ('product3', 200)]

list1.sort()
print('Ascending order sort: ', list1)
list1.sort(reverse=True)
print('Descending order sort: ', list1)

print("Original list: ", list2)
list2.reverse()
print("Reverse  list: ", list2)

list3 = list2.copy()
print("Copy list: ", list3)

list4 = list(list3)
print("Copy list using: ", list4)

# list filter and map methods using lambda methods
mappedList = list(map(lambda product: product[1], products))
print(f'mapped list using lambda fun: {mappedList}')
filteredList = list(filter(lambda product: product[1] > 100, products))
print(f'filteredList list using lambda fun: {filteredList}')
