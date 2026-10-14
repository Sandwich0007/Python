'''
Write a function that accepts an integer and prints whether it is odd
or even
'''
def odd_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num=int(input("Enter the number = "))
odd_even(num)