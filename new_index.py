def bSearch(a,p):
    l=0
    u=len(a)-1
    if(a[u]<p):
        return u+1
    while(l<=u):
        mid=(l+u)//2
        if(a[mid]==p):
            return mid
        elif(a[mid]<p):
            l=mid+1
        else:
            u=mid-1
    return l        