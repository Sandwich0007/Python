'''
Rearrage array element by sign
'''

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         pos = []
#         neg = []
#         for i in range(n):
#             if nums[i]>=0:
#                 pos.append(nums[i])
#             else:
#                 neg.append(nums[i])
#         for i in range(0,len(pos)):
#             nums[2*i]=pos[i]
#             nums[2*i+1]=neg[i]
#         return nums

'''
Optimal Solution
'''

class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0]*n
        posIndex, negIndex = 0,1
        for i in range(n):
            if nums[i]>= 0:
                result[posIndex]=nums[i]
                posIndex+=2
            else:
                result[negIndex]=nums[i]
                negIndex+=2
        return result