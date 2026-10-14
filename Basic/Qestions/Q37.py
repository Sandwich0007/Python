'''Leap Year'''

'''Wrong code'''

num=int(input("Enter the year: "))

if num%4==0 and num%100==0 and num%400==0:
    print(f"{num} is Leap Year")
else:
    print(f"{num} is not Leap Year ")