'''
Remove all the duplicates element from
that list.

my_list=[5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]

#OUTPUT
[5, 1, "Code and Debug", 10, 20]
'''
my_list=[5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]
result=[]
for i in range(0,len(my_list)):
    if my_list[i] not in result:
        result.append(my_list[i])
      
print(result)