'''
Two Sum
'''
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         # Check every pair (i, j)
#         for i in range(0,n-1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

'''
Optimal Solution
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining],i]
            hash_map[nums[i]] = i
        
