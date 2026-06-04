def unique_el_in_sorted_array(a):
    j=0
    for i in range (1, len(a)):
        if a[i]!=a[j]:
            a[j+1]=a[i]
            j=j+1

    return j        

