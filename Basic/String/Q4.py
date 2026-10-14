'''
Q134. Ask a string from user. Convert all the alphabets to lowercase
'''
# string=str(input("Enter the string = "))
# x = string.lower()
# print(x)

#ASCII METHOD

string=str(input("Enter the string = "))

for i in string:
    ascii = ord(i)
    if ascii >= 65 and ascii <=90:
        ascii + 32