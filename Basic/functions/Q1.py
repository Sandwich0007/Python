'''
Write a function that accepts an integer and prints the
multiplication table for that number up to 10.
'''
def multiplication(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

multiplication(5)