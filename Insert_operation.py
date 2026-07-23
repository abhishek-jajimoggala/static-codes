#Operations in array data structures
'''
1.insert at begin/end 
2.delete at begin/end
3.insert/delete by pos
4.delete by value
5.search
6.update
7.reverse
8.rotate left/right
'''

#insert at begin
'''n=3
arr=10 20 30
x=5
output:5 10 20 30'''
#built-in function for worst case side
'''arr=[10,20,30]
x=5
arr.insert(0,x)
print(arr)'''

arr=list(map(int,input("Enter values:").split()))
n=int(input("Enter a number to append at left:"))
arr.append(0)
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=n
print("Array append values is:",arr)