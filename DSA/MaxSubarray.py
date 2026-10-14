'''
Maximum SubArray
'''
# Brute force solution

# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         maxim = float("-inf")
#         for i in range(0,n):
#             sum = 0
#             for j in range(i,n):
#                 sum = sum + nums[j]
#                 maxim = max(maxi,sum)
#         return maxim

# Time Limit Will Exceed

'''
Optimal Solution
'''
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        maxi = float("-inf")
        sum = 0
        for i in range(0,n):
            sum = sum + nums[i]
            maxi = max(sum,maxi)
            if sum<0:
                sum = 0
        return maxi
           