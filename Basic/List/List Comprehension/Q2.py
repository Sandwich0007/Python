'''
Q122. Given a list of strings, create a new list containing the lengths of
each string using list comprehension.

# Example 1
my_list = ["apple", "banana", "orange", "kiwi"]
Sample Output: [5, 6, 6, 4]

# Example 2
my_list = ["done", "python", "", "ok bye"]
Sample Output: [4, 6, 0, 6]
'''
my_list = ["apple", "banana", "orange", "kiwi"]
lengths = [len(i) for i in my_list]
print(lengths)