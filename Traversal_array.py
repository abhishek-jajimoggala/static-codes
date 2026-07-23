#traversal in array data structures
'''arr=list(map(int,input("Enter the number of values:").split()))
print("Array elements added by 100")
for num in arr:
    print(num+100,end=' ')'''

#array minimum value
'''arr=list(map(int,input("Enter the number of values:").split()))
min= arr[0]
for i in arr:
    if i<min:
        min=i
print("Small value:",min)'''

#maximum and minimum number with 3x3 matrics of 2d array
'''rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
arr=[]
print("Enter matrix elements:")
for i in range(rows):
    row=list(map(int,input().split()))
    arr.append(row)
max=arr[0][0]
for i in range(rows):
    for j in range(cols):
        if arr[i][j]>max:
            max=arr[i][j]
print("Maximum element:",max)
min=arr[0][0]
for i in range(rows):
    for j in range(cols):
        if arr[i][j]<min:
            min=arr[i][j]
print("Minimum  element:",min)'''

#convert 2D into 1D array or linear data
'''rows=int(input("Enter a number of rows"))
cols=int(input("Enter a columns:"))
arr=[]
for i in range(rows):
    row=list(map(int,input().split()))
    arr.append(row)
for i in range(rows):
    for j in range(cols):
        print(arr[i][j],end=" ")'''

#reverse the data 1D array to 3D array
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
arr=list(map(int,input().split()))
matrix=[]
x=0
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(arr[x])
        x+=1
    matrix.append(row)
for row in matrix:
    print(*row)