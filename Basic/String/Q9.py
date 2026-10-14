'''
Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should
become "olleH dlroW"
'''
# string = input("Enter The String = ")
# words = string[::-1]
# print(words)

# 2nd Method

string = "This is string"
words = string.split()
result = " ".join(i[::-1] for i in words)
print(result)