'''
Q93. Make your own list. Print all the even numbers present in the list.

my_list = [51, 74, 85, 91, 52, 44]

Output
# 74 52 44
'''
#Iterate By Index
# my_list = [51, 74, 85, 91, 52, 44]

# for i in range(0,6):
#     if my_list[i]%2==0:
#         print(my_list[i],end=" ")

#Iterate By Value
my_list = [51, 74, 85, 91, 52, 44]
for i in my_list:
    if i%2==0:
        print(i,end=" ")
