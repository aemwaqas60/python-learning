list1 = [1, 2, 3, 4, 5, 6]

print('--- loop through a list using for loop ---- ')
for item in list1:
    print(item)

print('--- loop through a list using while loop ---- ')
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

print('----- Loop through a list using a index number -----')

for i in range(len(list1)):
    print(list1[i])
print('----- Loop through a list using list Comprehension -----')
[print(item) for item in list1]
