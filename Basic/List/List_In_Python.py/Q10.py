#Print how many positive and negative numbers are here

my_list=[1,2,3,4,0,-1,-2,-3,-4]
postive=0
negative=0
for i in my_list:
    if i>=0:
        postive=postive+1
    else:
        negative=negative+1

print(postive)
print(negative)
        




