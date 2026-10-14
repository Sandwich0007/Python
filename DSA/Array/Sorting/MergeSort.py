'''
Merge Sort
'''
class Solution:
    def mergeArr(self,left,right):
        result = []
        i,j=0,0
        n,m = len(left),len(right)
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        
        while i<n:
            result.append(left[i])
            i+=1
        
        while j<m:
            result.append(right[j])
            j+=1
        
        return result
        
                
    def mergeSort(self, arr):
      if len(arr)<=1:
          
          return arr
      mid = len(arr)//2
      left = arr[:mid]
      right = arr[mid:]
      left_sorted= self.mergeSort(left)
      right_sorted = self.mergeSort(right)
      return self.mergeArr(left_sorted,right_sorted)