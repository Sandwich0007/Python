'''
Intro of hashing
'''
# n = [1,2,3,4,4,5,2,6,7,5,6,8,7]
# m = [11,21,3,8,7,22,25,28,8,7,1]

# hash_list = [0]*11
# for num in n:
#     hash_list[num]+=1

# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

# Optimal Solution using Dictionary

# n = [1,2,3,4,4,5,2,6,7,5,6,8,7]
# m = [11,21,3,8,7,22,25,28,8,7,1]

# freq={}
# for item in n:
#     freq[item]=freq.get(item,0)+1

# for item in m:
#     print(freq.get(item,0))

# character hashing

# n = "alkjjdfuenvkerhvlwufonv"
# m = "ljweousvdoieglsdfasdlal"

# hashList = [0]*26

# for ch in n:
#     ascii_val = ord(ch)
#     index = ascii_val-97
#     hashList[index]+=1

# for ch in m:
#     ascii_val = ord(ch)
#     index = ascii_val-97
#     print(hashList[index])

# Optimal version of Character hashing usind dict

n = "alkjjdfuenvkerhvlwufonv"
m = "ljweousvdoieglsdfasdlal"

freq={}
for ch in n:
    freq[ch]=freq.get(ch,0)+1
for ch in m:
    print(freq.get(ch,0))


