def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if (arr[j]<arr[min]):
                min=j
        if(min!=i):
            temp=arr[i]
            arr[i]=arr[min]
            arr[min]=temp
    return arr
arr=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("Array before sorting:",arr)
print("Array after sorting:",selection_sort(arr))