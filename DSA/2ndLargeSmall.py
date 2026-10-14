'''
Find the second largest element in an array
'''
def getSecondOrderElements(n,a):
    largest = float("-inf")
    s_largest = float("-inf")

    

    for i in range(n):
        largest = max(largest, a[i])

    for i in range(n):
        if a[i] > s_largest and a[i] != largest:
            s_largest = a[i]

    return s_largest

a = [2,4,3,2,8,10]
n = len(a)

print(getSecondOrderElements(n,a))

'''
Find the second largest element and second smallest element in an array
'''
# def getSecondOrderElements(n,a)
#     # Write your code here.
#     largest = float("-inf")
#     s_largest = float("-inf")

#     smallest = float("inf")
#     s_smallest = float("inf")
#     n = len(a)
#     for i in range(n):
#         largest = max(largest,a[i])
#         smallest = min(smallest,a[i])
#     for i in range(n):
#         if a[i]>s_largest and a[i]!=largest:
#             s_largest = a[i]

#     for i in range(n):
#         if a[i]<s_smallest and a[i]!=smallest:
#             s_smallest = a[i]

#     return [s_largest,s_smallest]

# a = [4, 7, 2, 9, 9, 5]
# n = len(a)

# print(getSecondOrderElements(n, a))

   
        
