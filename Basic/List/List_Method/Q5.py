'''
Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.

my_list =[3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

Output
Odd = [3, 17, 35, 41]
Even = [8, 12, 22, 30, 48, 50]
'''
my_list =[3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
odd=[]
even=[]
for i in my_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)