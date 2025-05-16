# Debugging Exercises 

# Exercise 1: IndexError
# Fix the index error to correctly access the last element in the list
numbers = [1, 2, 3, 4, 5]
print(numbers[5])  # Error: IndexError: list index out of range

# Solution:
# print(numbers[4])


# Exercise 2: TypeError
# Fix the error by ensuring proper type conversion
num1 = '10'
num2 = 5
print(num1 + num2)  # Error: TypeError: can only concatenate str (not "int") to str

# Solution:
# print(int(num1) + num2)


# Exercise 3: KeyError
# Fix the KeyError by verifying the key exists in the dictionary
person = {'name': 'Alice', 'age': 30}
print(person['address'])  # Error: KeyError: 'address'

# Solution:
# print(person.get('address', 'Address not found'))


# Exercise 4: ValueError
# Fix the error by handling potential value conversion issues
value = 'abc'
print(int(value))  # Error: ValueError: invalid literal for int() with base 10

# Solution:
# try:
#     print(int(value))
# except ValueError:
#     print('Cannot convert to integer')


# Exercise 5: ZeroDivisionError
# Fix the division by zero error
numerator = 10
denominator = 0
result = numerator / denominator  # Error: ZeroDivisionError: division by zero

# Solution:
# if denominator != 0:
#     result = numerator / denominator
# else:
#     print('Cannot divide by zero')
