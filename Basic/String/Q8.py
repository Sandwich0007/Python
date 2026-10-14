'''
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.
'''
# string = "This is String"

# result = string.title()
 
# print(result)

# 2nd Method

string = "This is string"
words = string.split()
result = " ".join(i.title() for i in words)
print(result)
