'''
Write a program to find and print all 
prime numbers within a given list.
'''

list1=[2,3,4,5,6,7,8,13,15,17]
for i in list1:
    factors=0
    for num in range(1,i+1):
        if i%num==0:
            factors+=1
    if factors==2:
            print(i)
# my_list= [2, 5,7,8,9,10,11,13,17]
# for num in my_list:
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1
#     if factors == 2:
#             print(num)

