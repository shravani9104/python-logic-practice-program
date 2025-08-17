num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))
operator = input("enter operation (+, -, *, /, %) : ")

#perform operation
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)
elif operator == '%':
    if num2 == 0:
        print("Error: Cannot perform modulo with zero.")
    else:
        print("Result:", num1 % num2)
else:
    print("Invalid operator entered.")



