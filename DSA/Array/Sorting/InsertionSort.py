'''
Insertion Sort
'''

class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1]= arr[j]
                j= j-1
            arr[j+1]=key

        return arr

list1 = [2,1,5,4,8,5,6]
print(Solution().insertionSort(list1))

'''
Descending Insertion Sort
'''
# class Solution:
#     def insertionSort(self, arr):
#         n = len(arr)
#         for i in range(1,n):
#             key = arr[i]
#             j = i-1
#             while j>=0 and arr[j]<key:
#                 arr[j+1]= arr[j]
#                 j= j-1
#             arr[j+1]=key

#         return arr

# list1 = [2,1,5,4,8,5,6]
# print(Solution().insertionSort(list1))
