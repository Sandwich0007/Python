'''
Frequency in Dictionnary
'''

'''Brute'''

nums = [1,2,3,4,5,5,6,2,3,7,8,8,4]
my_dict = {}
for i in nums:
    if i not  in my_dict:
        my_dict[i]=1
    else: 
        my_dict[i]+=1

print(my_dict)


'''Optimal'''

# def frequency(num):
#     freq = {}
#     for item in num:
#         freq[item] = freq.get(item,0) + 1
#     return freq

# print(frequency([1,2,3,1,2,4,5,6,7,8,6]))