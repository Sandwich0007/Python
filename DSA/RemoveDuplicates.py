'''
Remove Duplicates from Sorted Array
'''
# class Solution:
#     def removeDuplicates(self, nums):
#         n=len(nums)
#         freq_map = {}
#         for i in range(n):
#             freq_map[nums[i]]=0
#         j=0 
#         for i in freq_map:
#             nums[j] = i
#             j+=1
#         return j
    
# nums = [1, 1, 2, 2, 3, 4, 4]
# k = Solution().removeDuplicates(nums)
# print(k, nums[:k])

# Optimal Solution:

class Solution:
    def removeDuplicates(self, nums):
        n=len(nums)
        i = 0
        for j in range(1,n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
            j+=1
        return i+1
nums = [1]
k= Solution().removeDuplicates(nums)
print(k, nums[:k])