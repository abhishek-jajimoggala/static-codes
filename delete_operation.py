#delete operation in array
'''capacity=20
arr=[0]*capacity
n=int(input("Enter the size of array(max:20):"))
for i in range(n):
    arr[i]=int(input(f"Enter element {i}:"))
size=n
pos=int(input("\n Enter the index value:"))
if size==0:
    print("Array is empty")
elif pos<0 and pos>=size:
    print("Invalid position ....")
else:
    deleted=arr[pos]
    for i in range(pos,size-1):
        arr[i]=arr[i+1]
    size-=1
    print("Deleted element:",deleted)
for i in range(size):
    print(arr[i],end=" ")'''


#Write a program to perform linear search in an array and print the index value found
arr=list(map(int,input("Enter a elements:").split()))
target=int(input("Enter the target"))
for i in range(len(arr)):
    if arr[i]==target:
        print(target,"Found at index value:",i)
        break
        
