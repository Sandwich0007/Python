'''
Missing Number
'''
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n+1):
#             if i not in nums:
#                 return i

'''
Better Solution
'''
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         freq={}
#         for i in range(n+1):
#             freq[i]=0
#         for num in nums:
#             freq[num]=1
#         for k,v in freq.items():
#             if v ==0:
#                 return k
'''
Optimal Solution
'''
class Solution:
    def missingNumber(self, nums): 
        n = len(nums)
        sum_of_n =(n*(n+1))/2
        sum_of_nums = 0
        for num in nums:
            sum_of_nums+=num

        return int(sum_of_n-sum_of_nums)       