# Count the number of even numbers present in
# that list.

#Iterate By Index

# my_list = [51, 85, 91.66, 52, 44, 100, 200]

# count=0
# for i in range(0,len(my_list)):
#     if my_list[i]%2==0:
#         count=count+1
# print(count)

#Iterate By Value

my_list = [51, 85, 91.66, 52, 44, 100, 200]
count=0
for i in my_list:
    if i%2==0:
        count=count+1

print(count)


# Output
# 4