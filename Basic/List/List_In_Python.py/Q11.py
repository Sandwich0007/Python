# Print the largest number present in that list.

my_list = [51, 85, 1748, 52, 44, 100, 200]
largest=my_list[0]
for i in range(0,len(my_list)):
    if my_list[i]>=largest:
        largest=my_list[i]

print(largest)

# Output
1748