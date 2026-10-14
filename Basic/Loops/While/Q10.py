#Calculate factorial of a number entered by user
num=int(input("Enter the number: "))
i=1
total=1
while i<=num:
    total=total*i
    i=i+1

print(total)