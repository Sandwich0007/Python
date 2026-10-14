'''
Q145. Write a Python program to multiply all the items in a dictionary
'''
my_dict = {"Code":10,"Debug":2,"value":3}
total = 1 
for i in my_dict.values():
    total = total * i
print(total)