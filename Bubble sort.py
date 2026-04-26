def  bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
#arr = [23, 5, 7, 2, 92, 64]
arr=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("Array before sorting:",arr)
print("The sorted array is:",bubble_sort(arr))
