def union (a,b):
    i=0
    j=0
    n=len(a)
    m=len(b)
    uni=[]
    while(i<n and j<m):
        if  a[i]<=b[j] :
            if len(uni)==0  or a[i] !=uni[-1]:           
             uni.append(a[i])
            i=i+1
        else:
           if len(uni)==0 or b[j] !=uni[-1]:
             uni.append(b[j])
           j=j+1
    while j<m:
        if len(uni)==0 or b[j] !=uni[-1]:
           uni.append(b[j])
        j=j+1
    while i<n :
        if len(uni)==0  or a[i] !=uni[-1]:
            uni.append(a[i])
        i=i+1   


    return uni         
a=[1,1,2,3,4]
b=[2,2,5]   
print(union(a,b))
        

