'''
Q26. A student will not be allowed to sit in exam if his/her attendance is
less than 75%.

Take following input from user
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
'''
class_held=int(input("Enter the number of classes held: "))
class_atnd=int(input("Enter the number of classes atnd: "))

pctg=(class_atnd/class_held)*100

print(f"Your attendance is {pctg:.2f}%")

if pctg>=75:
    print("Yes your are allowed to sit in exam")
else:
    print("No you are not allowed to sit in exam")

