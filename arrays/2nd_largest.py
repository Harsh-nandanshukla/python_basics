import sys
def second_largest(a):
    l=a[0]
    sl=-sys.maxsize-1
    for i in range (1,len(a)):
        if(a[i]>l):
            sl=l
            l=a[i]
        if(a[i]<l and a[i]>sl):
            sl=a[i]
    return sl
def second_smallest(a):
    s=a[0]
    ss= sys.maxsize            
    for i in range (1,len(a)): 
        if(a[i]<s):
            ss=s
            s=a[i]
        if(a[i]>s and a[i]<ss):
            ss=a[i]

    return ss            
a=[1,4,2,0]
print(second_smallest(a))