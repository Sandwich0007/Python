'''
Check if array is sorted or not
'''
class Solution:
    def isSorted(self, arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return False
            
        return True

print(Solution().isSorted([2,3,4,5,6]))