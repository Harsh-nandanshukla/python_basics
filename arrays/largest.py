def largest(a):
    if ( len(a)==0):
        return None
    lrgt=a[0]
    for i in range (len(a)):
        if(a[i]>lrgt):
            lrgt=a[i]

    return lrgt

a=[1,3,47,89,10]
print(largest(a))        