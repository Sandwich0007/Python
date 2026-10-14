'''
Q105. Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user.

my_list = [5, 10, 15, 20, 15]
Enter the old number: 15
Enter the new number: 25

Updated list: [5, 10, 25, 20, 25]
'''
my_list = [5, 10, 15, 20, 15]
old=int(input("Enter the old number: "))
new=int(input("Enter the new number: "))
for i in range(0,len(my_list)):
    if my_list[i]==old:
        my_list[i]=new


print(my_list)