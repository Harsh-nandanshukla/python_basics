def median(a):
    a=sorted(a)
    if len(a)%2!=0:
        return a[len(a)//2]
    else:
        return (a[(len(a)//2)-1]+a[len(a)//2])/2
a=[1,2,3,4,5,6]
print(median(a))