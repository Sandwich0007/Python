'''
Print one by one last digit of number
'''
n=3873
num=n
while num > 0:
    lst_digit = num%10
    print(lst_digit)
    num = num//10
