# a=int(input("Enter the first person age: "))
# b=int(input("Enter the second person age: "))
# c=int(input("Enter the third person age: "))
# max = a
# if max < b:
#     max=b
# if max < c:
#     max=c
# print(max)

# 2nd version
a=int(input("Enter the first person age: "))
b=int(input("Enter the second person age: "))
c=int(input("Enter the third person age: "))
oldest= max(a,b,c)

print(f"The oldest is {oldest}")