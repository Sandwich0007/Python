'''4SUM PROBLEM'''

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)

#         mySet = set()

#         for i in range(n): 
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     for l in range(k+1,n):
                        
#                         temp = nums[i]+ nums[j] + nums[k] + nums[l]
#                         if temp == target:
#                             temp = [nums[i], nums[j] , nums[k] , nums[l]]
#                             temp.sort()
#                             mySet.add(tuple(temp))

#         return [list(i) for i in mySet]

# Time limit will exceed in leetcode

'''Better Solution'''

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)

#         mySet = set()
        

#         for i in range(n): 
#             for j in range(i+1,n):
#                 hashSet = set()
#                 for k in range(j+1,n):
#                     fourth = target - (nums[i] + nums[j] + nums[k])
#                     if fourth in hashSet:
#                         temp = [nums[i],nums[j],nums[k],fourth]
#                         temp.sort()
#                         mySet.add(tuple(temp))
#                     hashSet.add(nums[k])

#         return [list(i) for i in mySet]

'''Optimal Solution'''

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if target == total:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif target < total:
                        l-=1
                    else:
                        k+=1
        return ans
                            

        

        