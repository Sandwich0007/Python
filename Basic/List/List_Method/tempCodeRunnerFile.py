list1=[2,3,4,5,6,7,8,13,15,17]
for i in list1:
    factors=0
    for num in range(1,i+1):
        if i%num==0:
            factors+=1
        if factors==2:
            print(i)