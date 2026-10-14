'''
All factors of a given number
'''

'''Brute'''

# n=532
# num = n
# factors = []
# for i in range(1,num+1):
#     if num%i==0:
#         factors.append(i)

# print(factors)

'''Better'''

# n=532
# num = n
# factors = []
# for i in range(1,(num//2)+1):
#     if num%i==0:
#         factors.append(i)
# factors.append(num)
# print(factors)

'''Optimal'''

from math import sqrt
n=50
num = n
factors = []
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        factors.append(i)
        if num//i!=i:
            factors.append(num//i)
print(factors)