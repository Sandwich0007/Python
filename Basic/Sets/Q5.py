'''
Write a Python program to check if two given sets have no elements
in common
'''
set1 = {1,2,3,4,5}
set2 = {0,6,7,8,9}

result = set1.intersection(set2)

if len(result)==0:
    print("Both sets have nothing in common")
else:
    print("They have something in common")
    print(result)
