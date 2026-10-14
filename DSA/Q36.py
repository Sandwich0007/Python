'''3SUM PROBLEM'''

# BRUTE FORCE

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         n = len(nums)
#         mySet = set()
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     temp = []
#                     if nums[i]+nums[j]+nums[k]==0:
#                         temp = [nums[i],nums[j],nums[k]]
#                         temp.sort()
#                         mySet.add(tuple(temp))
#         return [list(i) for i in mySet]

'''Better Solution'''

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         n = len(nums)
#         result = set()
#         for i in range(0,n):
#             mySet = set()
#             for j in range(i+1,n):
#                 third = - (nums[i]+nums[j])
#                 if third in mySet:
#                     temp = [nums[i],nums[j],third]
#                     temp.sort()
#                     result.add(tuple(temp))
#                 mySet.add(nums[j])

#         return [list(i) for i in result]

'''Optimal Solution'''

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            if i !=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                if total_sum>0:
                    k-=1
                elif total_sum<0:
                    j+=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return result

        