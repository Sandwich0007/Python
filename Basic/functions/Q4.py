'''
Write a function that takes an integer and 
prints whether it is a prime number
'''
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count += 1
    if count==2:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime")
prime(20)