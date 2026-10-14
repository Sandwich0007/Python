'''
137. Ask a string from user. Print the count of how many alphabets, digits,
     spaces and symbols (everything else) are there in that string
'''
string=str(input("Enter The String = "))

alphabets = 0
digits = 0
spaces = 0 
symbols = 0
for i in string:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        symbols += 1

print(f"alphabets is {alphabets}")
print(f"digits    is {digits}")
print(f"symbols   is {symbols}")
print(f"spaces    is {spaces}")
