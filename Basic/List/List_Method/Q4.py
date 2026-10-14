# Q107. Ask the user for a number. Then, from a list of numbers, remove all
# the numbers that can be divided by the number the user entered. (Do on
# your own).

# my_list = [10, 15, 20, 25, 30]
# Enter a number: 10

# # OUTPUT
# [15, 25]
my_list = [10, 15, 20, 25, 30]
new_list=[]
num=int(input("Enter The Number: "))

for i in my_list:
    if i%num!=0:
        new_list.append(i)

print(new_list)


