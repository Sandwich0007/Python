# Count how many numbers are divisible by both 2
# and 5 in that list. 

my_list = [51, 85, 91.66, 52, 44, 100, 200]
count=0
for i in range(0,len(my_list)):
    if my_list[i]%2==0 and my_list[i]%5==0:
        count=count+1
print(count)


# Output
# 2