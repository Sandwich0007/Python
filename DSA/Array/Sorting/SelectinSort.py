'''
Selection sort using recurion
'''
class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            max_index = i
            for j in range(i+1,n):
                if arr[max_index]>arr[j]:
                    max_index = j
            arr[i],arr[max_index] = arr[max_index],arr[i]
        return arr

arr=[4,3,7,6,8,1,9]
print(Solution().selectionSort(arr))