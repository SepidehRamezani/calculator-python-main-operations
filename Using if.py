# A simple calculator which does the 4 main operations (as you want) by the given numbers.
# if / elif / else

a = int (input("This is a calculator. Please enter your first number:\n"))
c = input ("Enter your operator:")
b = int (input("Enter your second number:"))
if c == "+":
    print (a+b)
elif c == "-":
    print (a-b)
elif c == "*":
    print (a*b)
else:
    print (a//b)