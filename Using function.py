# A simple calculator which has does the 4 main operators (as you want) by the given numbers.
# if / elif / else / function

def calculate():
    a = int (input("This is a calculator. Please enter your first number:\n"))
    c = input ("Enter your operator:")
    b = int (input("Enter your second number:"))
    if c == "+":
        print('{} + {} = '.format(a,b),(a+b))
    elif c == "-":
        print('{} - {} = '.format(a,b),(a-b))
    elif c == "*":
        print('{} ‎×‎ {} = '.format(a,b),(a*b))
    else:
        print('{} ‎÷‎ {} = '.format(a,b),(a//b))
calculate()