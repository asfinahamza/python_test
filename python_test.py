n=int(input("enter limit "))
ps=int(input("enter the number to be checked "))
ar=[]
for x in range(n):
    ar.append(int(input("enter value ")))
ar.sort()
print(ar)
def index(a,p):
    for y in range(len(a)):
        if(a[y]>p):
            print("index: ",y)
            break
index(ar,ps)



