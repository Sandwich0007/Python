'''
Q136. Count the number of spaces in a string entered by user.
'''
string="lfj lsf l"
count = 0
for i in string:
    
    if ord(i) == 32:
        count += 1
        
print(count)