print("Calculator")

first_number = int(input('Number1: '))
operator = input('Sign: ')
second_number = int(input('Number2: '))


if operator == '+':
    results = first_number + second_number
if operator == '-':
    results = first_number - second_number
if operator == '*':
    results = first_number * second_number
if operator == '/':
    results = first_number / second_number

print(f"{first_number} {operator} {second_number} = {results}")