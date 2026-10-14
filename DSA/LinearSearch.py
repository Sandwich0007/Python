'''
Implementing Linear Search
'''
def liner(arr):
    target = 4
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[1,2,3,4,5]
print(liner(arr))