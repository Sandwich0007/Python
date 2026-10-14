'''
Longest consecutive sequence
'''

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_count = 0 
#         for i in range(n):
#             num = nums[i]
#             count =1
#             while num+1 in nums:
#                 count+=1
#                 num+=1
#             max_count = max(max_count,count)

#         return max_count

# Time Limit Exceeded

'''Better Solution'''

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         last = float("-inf")
#         max_count = 0 
#         count = 1
#         for i in range(n):
#             num=nums[i]
#             if num-1 == last:
#                 count+=1
#                 last = num
#             elif num!= last:
#                 last = num
#                 count=1
#             max_count = max(max_count,count)

#         return max_count

'''
Optimal Solution
'''
class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        mySet = set()
        for i in range(n):
            mySet.add(nums[i])
        maxCount = 0
        for num in mySet:        
            if num-1 not in mySet:
                count = 1  
                while num+1 in mySet:
                    count+=1
                    num+=1
                maxCount = max(maxCount,count)
        return maxCount



        