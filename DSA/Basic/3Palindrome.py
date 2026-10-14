'''
Check if a number is palindrome or not
'''
n = 121
num = n
result = 0
while num > 0:
    Ld = num%10
    result = (result*10) + Ld
    num = num//10
if result==n:
    print("Palindrome")
else:
    print("Not Palindrome")
   