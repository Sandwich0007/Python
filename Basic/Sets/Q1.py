'''
Given two lists a, b. Check if two lists have at least one element
common in them
'''

a = [2,3,4,5]
b = [9,6,7,8]

set1 = set(a)
set2 = set(b)

if set1.intersection(set2):
    print("Yes the have common element")
else:
    print("No common element")