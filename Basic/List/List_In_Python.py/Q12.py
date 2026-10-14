# Print the smallest number present in that list.

my_list = [51, 85, 1748, 52, 44, 100, 200]
smallest=my_list[0]
for i in range(0,len(my_list)):
    if my_list[i]<=smallest:
        smallest=my_list[i]

print(smallest)
