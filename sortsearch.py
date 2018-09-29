def sortSearch(matrix,k,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j]==k:
                print("Elements found at row {0} and column {0}".format(i,j))




m=int(input("enter no of rows"))
n=int(input("Enter no of columns"))
matrix=[[0 for j in range(n)] for i in range(m)]
print("Enter matrix elements")
for i in range(0,m):
    for j in range(0,n):
        matrix[i][j]=int(input())
print("Enter element to search")
k=int(input())
sortSearch(matrix,k,m,n)
