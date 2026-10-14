'''
Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order
my_list=[5, 1, 5, 10, 20, 5, 1, 1]

# Output
another_list = [1, 1, 5, 20, 10, 5, 1, 5]
'''
my_list=[]

for i in range(10):
    num=int(input("Enter the number: "))
    my_list.append(num)

result=[]   
for i in range(len(my_list)-1,-1,-1):
    result.append(my_list[i])
    

print(result)
# my_list=[]
# result=[]
# for i in range(5):
#     num=int(input("Enter the number: "))
#     my_list.append(num)
#     result=my_list.copy()
#     result.reverse()
    

# print(result)

    