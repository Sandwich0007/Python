'''
Q111. Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1.

my_list=[5, 1, 5, 10, 20, 5, 1, 1]

Enter value = 10
# OUTPUT = 3

Enter value = 5
# OUTPUT = 0

Enter value = 100
# OUTPUT = -1
# '''
my_list=[5, 1, 5, 10, 20, 5, 1, 1]
num=int(input("Enter the Number: "))
if num in my_list:
        index=my_list.index(num)
        print(f"The Index of Number {num} is {index}")
else:
        print(-1)