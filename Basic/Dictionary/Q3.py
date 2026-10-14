'''
Q144. Write a Python program to sum all the items in a dictionary
'''

my_dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# total = 0
# for i in my_dict.values():
#     total = total + i

# print(total)

print(sum(list(my_dict.values())))