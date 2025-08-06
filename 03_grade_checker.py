marks = int(input("enter marks:"))

if marks < 0  :
    print("Invalid Marks")
elif marks > 100 :   
    print("Invalid Marks") 
elif marks >= 90 :  
    print("Your grade is: A+")
elif marks >= 80  :
    print("Your grade is: A")
elif marks >= 70 :
    print ("Your grade is: B")
elif marks >= 60 :  
    print("Your grade is: C")

else:
    print("You have Failed. Better luck next time!")