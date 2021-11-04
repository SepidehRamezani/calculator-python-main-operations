# A simple calculator which does the 4 main operations (all at once) by the given numbers.
# {}.format

a = int (input("This is a calculator. Please enter your first number:\n"))
b = int (input("Enter your second number:"))
print('{} + {} = '.format(a,b),(a+b))
print('{} - {} = '.format(a,b),(a-b))
print('{} ‎×‎ {} = '.format(a,b),(a*b))
print('{} ‎÷‎ {} = '.format(a,b),(a//b))