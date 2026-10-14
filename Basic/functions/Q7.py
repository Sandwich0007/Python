'''
Write a function that takes a string 
and prints whether it is a palindrome
'''
def check_palindrome(string):
    if string==string[::-1]:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not palindrome")

check_palindrome("mom")