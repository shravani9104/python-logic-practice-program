n = int(input(" Enter a number :  "))

# Store original number
original = n 

# Find sum of cubes of digits
sum_of_cubes = 0
while n > 0:
    digit = n % 10 
    sum_of_cubes += digit ** 3 
    n //= 10

# Compare with original number
if original == sum_of_cubes:
    print(original, "is an Armstrong number. ")
else:
    print(original, "is Not an Armstrong number.")