'''
Q132. Ask a string from user. Count how many
      alphabets are there in that string
'''

string=str(input("Enter the String "))
count=0
for i in string:
    ascii=ord(i)
    if (ascii >= 65 and ascii <=90) or (ascii>=97 and ascii<=122):
        count=count+1
    
print(count)