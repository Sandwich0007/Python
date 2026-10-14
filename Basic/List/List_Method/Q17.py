'''
Write a python program to swap first element from last element of list
'''
list1 = [1,2,3,4,5,6]
list1[0],list1[-1] = list1[-1],list1[0]

print(list1)