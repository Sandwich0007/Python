'''
Q31. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid
'''

num=int(input("Enter the bill amount: "))

if num>=50000:
    discount=30
elif num>=40000 and num<50000:
    discount=25
elif num>=30000 and num<40000:
    discount=20
elif num>=10000 and num<30000:
    discount=10
else:
    discount=0

print(f"Your total discount is {discount}%")

final_bill=num-(num*discount)/100

print("Your final bill after discount ",final_bill)
 