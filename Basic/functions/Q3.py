'''
Write a function that takes three numbers as 
parameters and prints the largest among them
'''
def largest(a,b,c):
    if a>b and a>c:
        print("A is the largest")
    elif b>a and b>c:
        print("B is the largest")
    else:
        print("c is the largest")

largest(2,2,2)