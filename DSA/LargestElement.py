''' 
Find the largest element in an array
'''

class Solution:
    def largest(self, arr):
        n = len(arr)
        # biggest = float("-inf") 2nd method
        biggest = arr[0]
        for i in range(0,n):
            if arr[i]>biggest:
                biggest = arr[i]
                
        return biggest
   
        
