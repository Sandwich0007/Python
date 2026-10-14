#Calculate factorial of a number entered by user
total=1
num=int(input("Enter the number: "))
for i in range(1,num+1):
    total=total*i

print(total)
