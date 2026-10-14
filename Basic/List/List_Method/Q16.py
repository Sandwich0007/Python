'''
Write a program to split a given list into two halves
'''

list1=[1,2,3,4,5,6,7,8,9]
mid=len(list1)//2
first_half=list1[:mid]
second_half=list1[mid:]

print(first_half)
print(second_half)
