'''
Write a Python code to find the occurrence of each element
in a list and print the element with the highest occurrence
'''
my_list=[2,4,7,8,2,2,9,7,6,4]
new_list=[]


for i in my_list: 
    if i not in new_list:
        new_list.append(i)
highest_elmnt_occur=0
highest_occurence=0

for num in new_list:
    x=my_list.count(num)
    if x>highest_occurence:
        highest_occurence=x
        highest_elmnt_occur=num
    print(f"Occurance of {num} is {x} times")
print("Highest occurence element ",highest_elmnt_occur)
print("Highest occurence is ",highest_occurence)
