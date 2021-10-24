n=int(input("enter limit "))
ps=int(input("enter the number to be checked "))
ar=[]
for x in range(n):
    ar.append(int(input("enter value ")))
ar.sort()
print(ar)
def bSearch(a,p,l,u):
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
print(bSearch(ar,ps,0,n-1))