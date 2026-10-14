# Q53. Ask to numbers x and y from the user. If x<y then print all the
# numbers from x to y, but if y<x then print all the numbers from y to x

x=int(input("Enter the number x: "))
y=int(input("Enter the number y: "))

if x<y:
    while x<=y:
        print(x,end=" ")
        x=x+1
else:
    while y<=x:
        print(y,end=" ")
        y=y+1

