'''
Q128. Implement a python program to get the last 'n' elements from a list
using slicing.

a = [23, 54, 78, 43, 12, 34, 89]

# Example 1
Enter n = 3
Output = [12, 34, 89]

# Example 2
Enter n = 2
Output = [34, 89]'''

a = [23, 54, 78, 43, 12, 34, 89]
n = int(input("Enter the last n elements you want: "))  

last_n_elements = a[-n:]
print(last_n_elements)
