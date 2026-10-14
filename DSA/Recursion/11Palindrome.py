# '''
# Palindrome of string using recursion
# '''
# def recursion(s,left,right):
#     if left>=right:
#         return True
#     if s[left]!=s[right]:
#         return False
#     return recursion(s,left+1,right-1)

# def palindrome_recursion(s):
#     return recursion(s,0,len(s)-1)
    
# print(palindrome_recursion("racecar"))
# print(palindrome_recursion("hello"))

'''
Check if string is palindrome using recursion
'''
def pal(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return pal(s,left+1,right-1)

s = "madam"
print(pal(s,0,len(s)-1))
