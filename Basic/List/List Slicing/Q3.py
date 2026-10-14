'''
Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half
'''
list1 = [1,2,3,4,5,6,7,8,9]
divide = len(list1)//2
new_list1 = list1[:divide]
new_list2 = list1[divide:]
print(new_list1)
print(new_list2)