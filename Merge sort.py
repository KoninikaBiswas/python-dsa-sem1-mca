def mergesort(a,lb,ub):
    if lb<ub:
        mid=((lb+ub)//2)
        mergesort(a,lb,mid)
        mergesort(a,mid+1,ub)
        merge(a,lb,mid,ub)
    return a
def merge(a,lb,mid,ub):
    b=[0]*len(a)
    i=lb
    j=mid+1
    k=lb
    while i<=mid and j<=ub:
        if a[i]<=a[j]:
            b[k]=a[i]
            i=i+1
            k=k+1
        else:
            b[k]=a[j]
            j=j+1
            k=k+1
    if i>mid:
        while(j<=ub):
            b[k]=a[j]
            j=j+1
            k=k+1
    else:
        while(i<=mid):
            b[k]=a[i]
            i=i+1
            k=k+1
    for k in range(lb,ub+1):
        a[k]=b[k]
a=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    a.append(element)
print("Array before sorting:",a)
print("Array after sorting:",mergesort(a,0,len(a)-1))

