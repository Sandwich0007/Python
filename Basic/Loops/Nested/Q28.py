'''
Enter the number: 6
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,6):
        print(i,end=" ")
    print()