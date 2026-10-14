'''Calculate how many numbers are divisible by both 6 and 7 between 1
to 200'''

count=0
for i in range(1,201):
    if i%7==0 and i%6==0:
        count=count+1

print(count)