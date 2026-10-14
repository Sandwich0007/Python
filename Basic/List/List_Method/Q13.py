'''
Write a Python code to find the second largest
element in a list without sorting
'''
list1=[20,40]
largest=float("-inf")
second_largest=float("-inf")
for i in range(0,len(list1)):
    if list1[i] > largest:
        second_largest=largest
        largest=list1[i]
        
    elif list1[i] > second_largest and list1[i] < largest:
        second_largest=list1[i]

print(f"The Second largest Number is List is {second_largest}")

# my_list = [54, 32, 17, 67, 43, 11, 87,87, 44, 54, 32]
# largest = float("-inf")
# second_largest = float("-inf")

# for num in my_list:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num < largest:
#         second_largest = num

# print(second_largest)