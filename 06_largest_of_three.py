a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

if a >= b and a >= c : 
    print("The Largest number is : ", a )
elif a <= b and b >= c : 
    print("The Largest number is : ", b )
else:
    print("The Largest number is : ", c)
