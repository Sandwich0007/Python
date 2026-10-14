# Q104. Write a program that prompts the user to specify the length of a list
# and then requests numbers to populate that list. Display the final list as
# the output.

# # Example
# Input the length of the list: 4
# Enter number = 7
# Enter number = 14
# Enter number = 21
# Enter number = 28

# Answer = [7, 14, 21, 28]

lenght=int(input("Enter the length of List: "))
result=[]

for i in range(1,lenght+1):
    num=int(input(f"Enter the number at {i} position: "))
    result.append(num)

print(result)
