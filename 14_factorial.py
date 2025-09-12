n = int(input("Enter a number: "))

# Factorial is not defined for negative numbers
if n < 0:
    print("Factorial is not defined for negative numbers.")

# Factorial of 0 and 1 is always 1
elif n == 0 or n == 1:
    print("Factorial:", 1)
else:
    fact = 1  
    for i in range(1, n + 1):  
        fact *= i  # multiply fact by each i
    print("Factorial:", fact)