#Ask start number and end number from user. Print all the numbers
#from start to end using while loop

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))

for i in range(start,end+1):
    print(i)