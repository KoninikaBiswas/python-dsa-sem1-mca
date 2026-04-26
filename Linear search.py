arr=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("The array is:",arr)
data=int(input("Enter the data to be searched: "))
for i in range(n):
    if arr[i]==data:
        print("Element found at index:",i)
        break
else:
    print("Element not found!")

