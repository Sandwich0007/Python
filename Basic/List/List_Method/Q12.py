'''
Q115. Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.

Example 1
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
# Output
[3, 4, 5]

# Example 2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# Output
[5, 6, 7, 8, 9, 10]'''
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result=[]
for i in list1:
    if i in list2:
        if i not in result:
            result.append(i)

print(result)