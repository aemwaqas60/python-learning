# age = int(input('Age: '))
# try:
#     with open('functions.py') as file, open('lists.py') as target:
#         xFactor = 10 / age
# except (ZeroDivisionError, ValueError):
#     print(f'You did not enter a valid input')
# else:
#     print('No exceptions were thrown')
#

# throw custom errors
def calculateXFactor(age):
    if age <= 0:
        raise ValueError('input can not be 0 or negative')
    else:
        return 10 / age


try:
    age = int(input('Age: '))
    calculateXFactor(age)
except ValueError as error:
    print(f'Error: {error}')
