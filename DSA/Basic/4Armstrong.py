'''Armstrong Number'''

n = 152
num = n
count = len(str(num))
total = 0
while num>0:
    ld = num%10
    total = total + (ld**count)
    num = num//10

if total == n:
    print("Armstrong number")
else:   
    print("Not Armstrong Number")
