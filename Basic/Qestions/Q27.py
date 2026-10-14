'''
Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero
'''
num=int(input("Enter the number: "))

if num==0:
    print("Equal to Zero")
elif num%2==0:
    print("Even")
else:
    print("Odd")