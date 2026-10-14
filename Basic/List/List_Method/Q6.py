'''
Q109. Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together.

list1 = [5, 8, 12, 15]
list2 = [3, 10, 18, 21]

# OUTPUT
Merged list: [5, 8, 12, 15, 3, 10, 18, 21]
'''
list1 = [5, 8, 12, 15]
list2 = [3, 10, 18, 21]
list3 = []
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
print(list3)
