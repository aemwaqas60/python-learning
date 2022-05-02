fruits = ['apple', 'orange', 'mango', 'pineapple']
apple, *others, pineapple = fruits

print(apple, pineapple, others)

# index, value unpacking using enumerate(return tuple (index, value))

for index, value in enumerate(fruits):
    print(f'index  {index}, value {value}')
