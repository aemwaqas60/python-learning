# normal function
def greetings():
    print('Welcome to python functions!')


# function with arguments and default parameters
def multiply(number1, number2=1):
    return number1 * number2


# function with unlimited number of parameters, python package them tuples
def cal_total(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# keyword parameter function
def greetings_fun(first_name, last_name):
    print(f' Welcome {first_name}  {last_name}')


# function parameters with key-value paris, python package them in dictionaries
def save_user(**user):
    print(f' id : {user}')


# fizz buzz problem solution
def fizz_buzz(input_number):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return 'fizzBuzz'
    if input_number % 3 == 0:
        return 'fizz'
    if input_number % 5 == 0:
        return 'buzz'
    return input_number


# function calling with optional
# print(multiply(2, 2));
# print(multiply(7))

# function calling with keyword arguments
# greetings_fun(first_name='Muhammad', last_name='Waqas')

# function with unlimited number of arguments
# print('Total: ', cal_total(1, 2, 3, 4, 5))

# function calling with key-value paris or keyword arguments
# save_user(id=1, name='Muhammad Waqas', age=29)

# fizz buzz fun calling with input
print('fizz buzz output: ', fizz_buzz(15))
