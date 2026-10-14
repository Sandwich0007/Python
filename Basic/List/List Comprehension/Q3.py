# Q123. Generate a list of strings where each string repeats itself three times,
# using list comprehension.

# # Example 1
# my_list = ['a' , 'b', 'c']
# Sample Output: ['aaa' , 'bbb', 'ccc' ]

# # Example 2
# my_list = ['xyz' , 'zz', 'ab' ]
# Sample Output: ['xyzxyzxyz' , 'zzzzzz' , 'ababab' ]
my_list = ['a' , 'b', 'c']
new_list = [i*3 for i in my_list]
print(new_list)