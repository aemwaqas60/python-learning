age = 25
highIncome = True
goodCredit = True
student = False
success = False

# ternary operator
message = 'Eligible' if age >= 18 else 'Not Eligible';

# logical operators
if (highIncome or goodCredit) and not student:
    message = 'Eligible for loan'
else:
    message = 'Not Eligible for loan'

# chaining comparison
if 18 <= age < 65:
    message = 'Eligible'

print(message)
# for loop with else
count = 0
for number in range(5):
    print(f"attempt {number + 1}")
    count += 1
    if success:
        break
else:
    print(f'Attempted  {count} time, but Unsuccessful')
