#Ask a number from user. Print the multiplication table of that number

num=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
