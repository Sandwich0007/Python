'''
Move zeroes to the end of the list
'''

# class Solution:
#     def moveZeroes(self,nums):
#         n = len(nums)
#         temp = []
#         for i in range(0,n):
#             if nums[i]!=0:
#                 temp.append(nums[i])
#         nt = len(temp)
#         for i in range(0,nt):
#             nums[i] = temp[i]
#         for i in range(nt,n):
#             nums[i]=0
#         return nums

# print(Solution().moveZeroes([1,2,3,4,0,5,0,4,5,0]))

'''
Optimal Solution
'''
def moveZeroes(arr):
    n = len(arr)

    if n == 1:
        return arr

    i = 0

    while i < n:
        if arr[i] == 0:
            break
        i += 1

    if i == n:
        return arr

    j = i + 1

    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    return arr


print(moveZeroes([1,2,3,4,0,5,0,4,5,0]))
        
