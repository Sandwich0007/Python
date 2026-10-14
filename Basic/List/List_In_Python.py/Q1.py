'''
Make your own list. Print the list in reverse.

my_list = [4, -98, "Code and Debug", 22.22, 100]

# Output
# 100 22.22 "Code and Debug" -98 4
'''
#Iterate By Index

my_list = [4, -98, "Code and Debug", 22.22, 100]
for i in range(len(my_list)-1,-1,-1):
    print(my_list[i],end=" ")

