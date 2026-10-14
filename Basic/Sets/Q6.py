'''
Write a Python program to find elements in a given set that are not
in another set
'''
set1 = {1,2,3,4,5}
set2 = {2,3,6,7,8}

result = set1.difference(set2)
print(result)