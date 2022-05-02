import math

# strings and string methods
courseName = '  Python Programming    '

# string slicing
print(courseName[0])
print(courseName[0:])
print(courseName[0:-1])
print(courseName[:-1])
print(courseName[:])

# string methods
print('----------- String Methods ------------')
print(f'string Length: {len(courseName)}')
print(courseName.upper())
print(courseName.lower())
print(courseName.capitalize())
print(courseName.strip())
print(courseName.rstrip())
print(courseName.lstrip())
print(courseName.find('pro'))
print(courseName.find('m'))
print('-----------------------------------------')

# in and not operator execute statement and return Ture or False
print('------- in and not operators -----------')
print("pro" in courseName)
print("pro" not in courseName)
print('----------------------------------------')

print('------------ Type Conversion ------------')
# int()
# float()
# str()
# bool()
# age = input('Enter your age: ')
# num = int(age) + 1
#
# print(f'age + 1 = {num}')
print('------------------------------------------')

print(f'math ceil 23: {math.ceil(23.3)}')
print(f'math floor 12.6:  {math.floor(12.6)}')
print(f'absolute -10:  {abs(-10)}')
print(f'round: 2.9:  {round(2.9)}')
