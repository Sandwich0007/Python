'''
Right rotate an array by one place
'''
# def rotate_array(arr):
#     n = len(arr)
#     arr[:] = [arr[n-1]] + arr[0:n-1]
#     return arr

# print(rotate_array([1,2,3,4]))

# without using slice

# def rotate_array(arr):
#     n=len(arr)
#     temp = arr[n-1]
#     for i in range(n-2,-1,-1):
#         arr[i+1] = arr[i]   
#     arr[0]=temp
#     return arr

# print(rotate_array([1,2,3,4]))

'''
rotate the array to the right by k steps
'''
# class Solution:
#     def rotate(self, nums,k):
#         n = len(nums)
#         k = k%n
#         for _ in range(k):
#             e = nums.pop()
#             nums.insert(0,e)
#         return nums
    
# print(Solution().rotate([1,2,3,4,5,6,7,8,9],3))

'''
By usng slice
'''
# class Solution:
#     def rotate(self, nums,k):
#         n = len(nums)
#         k = k%n
#         nums[:]=nums[n-k:] + nums[:n-k] 
#         return nums

# print(Solution().rotate([1,2,3,4,5,6,7,8,9],3))

'''
Without using python features'''

def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1

def rotate(arr, k):
    n = len(arr)
    k = k % n

    # Reverse whole array
    reverse(arr, 0, n - 1)

    # Reverse first k elements
    reverse(arr, 0, k - 1)

    # Reverse remaining elements
    reverse(arr, k, n - 1)

    return arr


print(rotate([1,2,3,4,5,6,7,8,9], 3))
