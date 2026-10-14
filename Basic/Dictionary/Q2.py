'''
Q143. Convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary.

lst1 = ['Ten', 'Twenty', 'Thirty' ]
lst2 = [10, 20, 30]

# Output
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''

lst1 = ['Ten', 'Twenty', 'Thirty' ]
lst2 = [10, 20, 30]

result = {}
for i in range(0,len(lst1)):
    result[lst1[i]] = lst2[i]
print(result)