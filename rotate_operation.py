#rotate a array-left
'''arr=list(map(int,input("Enter values:").split()))
k=int(input("Enter k:"))
n=len(arr)
if n>0:
    k=k%n
rotated=arr[k:]+arr[:k]
print(rotated)'''

'''arr=list(map(int,input("Enter values:").split()))
k=int(input("Enter k:"))
n=len(arr)
#if n>0:
#   k=k%n
rotated=[]
for i in range(k,n):
    rotated.append(arr[i])
for i in range(0,k):
    rotated.append(arr[i])
print(rotated)'''

#rotate of right position
'''arr=list(map(int,input("Enter values:").split()))
k=int(input("Enter k:"))
n=len(arr)
#if n>0:
#   k=k%n
rotated=[]
for i in range(n-k,n):
    rotated.append(arr[i])
for i in range(0,n-k):
    rotated.append(arr[i])
print(rotated)'''

#array of reverse
'''arr=list(map(int,input("Enter values:").split()))
n=len(arr)
reversed=[]
for i in range(n-1,-1,-1):
    reversed.append(arr[i])
print(reversed)'''

#2nd largest element in reverse order
arr= list(map(int, input("Enter values").split()))
large=None
second=None
for num in arr:
    if large is None:
        large=num
    elif num>large:
        second=large
        large=num
    elif num!=large and (second is None or num>second):
        second=num
print(second)