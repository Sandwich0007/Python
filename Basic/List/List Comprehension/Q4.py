'''
Generate a list of list using list comprehension where format should
be [[1, "ODD"], [2, "EVEN"], [3, "ODD"]].

# From 1 to 5
[[1, 'ODD'], [2, 'EVEN' ], [3, 'ODD' ],
[4, 'EVEN'], [5, 'ODD']]
'''
list1 = [[i ,"Even" if i%2==0 else "Odd"]for i in range(1,6)]
print(list1)