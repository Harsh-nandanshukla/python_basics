def move_zeroes(a):
    j=-1
    for i in range (len(a)):
        if a[i]==0:
            j=i
            break
    if (j==-1):
        return None
    for i in range (j+1,len(a)):
        if a[i]!=0:
            a[j],a[i]=a[i],a[j]
            j=j+1
    return a        

nums=[1,2,0,0,3]
print(move_zeroes(nums))            

        

