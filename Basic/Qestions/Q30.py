'''
Q30. Write a program to check if the last digit of a number is divisible by 5
or not'''

num=int(input("Enter the number: "))

lst_dgt=num%10

if lst_dgt%5==0:
    print("Yes it is divisible by 5")
else:
    print("Not possible")