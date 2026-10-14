'''
Reverse an array using recursion
'''
# nums = [1,2,3,4,5,6,7,8,9]
# def func(nums,l,r):
#     if l>=r:
#         return
#     nums[l],nums[r]=nums[r],nums[l]
#     func(nums,l+1,r-1)

# r=len(nums)-1

# func(nums,2,5)
# print(nums)


''' 
reverse an array normal method
'''
# arr = [3,8,2,4,9,1,0,9,7,8]

# arr[2:6] = arr[2:6][::-1]

# print(arr)

'''
reverse an array using while loop
'''

# nums = [1,2,3,4,5,6,7,8,9]
# l=0
# r=len(nums)-1
# while l<r:
#     nums[l],nums[r]=nums[r],nums[l]
#     l+=1
#     r-=1
# print(nums)

'''
Check if string is palindrome
'''

# s = "nitin"

# reverse = s[::-1]

# if s==reverse:
#     print(True)
# else:
#     False

'''
Check if string is palindrome using while loop
'''

# def palindrom(s):
#     left = 0
#     right =len(s) - 1
#     while left<right:
#         if s[left] != s[right]:
#             return False
        
#         left+=1
#         right-=1
    
#     return True

# print(palindrom("madam"))








