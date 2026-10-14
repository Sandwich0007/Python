# def AllFactor(n):
#     factor = []
#     for i in range(1,n+1):
#         if n%i==0:               
#             factor.append(i)
#     return factor

# n = int(input("Enter number: "))
# print(AllFactor(n))

# Better solution
# def AllFactor(n):
#     factor = []
#     for i in range(1,n//2):
#         if n%i==0:               
#             factor.append(i)
#     factor.append(n)
#     return factor

# n = int(input("Enter number: "))
# print(AllFactor(n))
    
# Optimal Solution
from math import sqrt
def allfactor(n):
    result = []
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if n//i!=i:
                result.append(n//i)
    result.sort()
    return result

n= int(input("Enter the number "))
print(allfactor(n))
    