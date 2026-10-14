'''
Write a program to reverse the order of words
'''

string = "How You Are Doing"


words = string.split()
words = words[::-1]
result =" ".join(words)
print(result)

