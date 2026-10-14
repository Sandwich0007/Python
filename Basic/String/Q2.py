'''
Q133. Ask a string from user. Count the number of uppercase
            and lowercase characters in that String.
'''
string=str(input("Enter the string "))
upper = 0
lower = 0
for i in string:
    ascii = ord(i)
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
    if ascii>=65 and ascii<=90:
        upper += 1
    elif ascii>=97 and ascii<=122:
        lower += 1


print(upper)
print(lower)