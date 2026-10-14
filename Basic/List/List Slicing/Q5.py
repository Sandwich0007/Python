'''
Q129. Ask ‘n’ from user. Create a list of last n 
elements but in reverse order using slicing
'''
my_list = [23, 54, 78, 43, 12, 34, 89]

n = int(input("Enter how many last elements you want: "))

# take last n elements and reverse them using slicing
result = my_list[-n:][::-1]

print("Last", n, "elements in reverse order:", result)
