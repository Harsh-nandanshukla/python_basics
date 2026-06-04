def rotate_right_optimal(a,k):
    n=len(a)
    a.reverse()
    a[0:k]=a[0:k][::-1]
    a[k:n]=a[k:n][::-1]
    return a
def roatate_left_optimal(a,k):
    n=len(a)
    a[0:k]=a[0:k][::-1]
    a[k:n]=a[k:n][::-1]
    a.reverse()
    return a
print(rotate_right_optimal([1,2,3,6,7],2))