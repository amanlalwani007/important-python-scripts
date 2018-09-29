#merge two subarrays of arr[]
#first subarray is arr[1..m]
#second subarray is arr[m+1..r]
def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    #create temp arrays

    #copy data to temp arrays l[] and r[]
    for i in range(0,n1):
        l[i]=arr[1+i]
    for j in range(0,n2):
        r[j]=arr[m+1+j]
    i=0
    j=0
    k=1
    while i<n1 and j<n2:
        if l[i]<=r[j]:
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=l[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=r[j]
        j+=1
        k+=1


def mergeSort(arr,l,r):
    if l<r:
        m=(l+(r-1))/2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,1,m,r)
#Driver code to test above
arr=[12,11,13,5,6,7]
n=len(arr)
print("given array is ")
for i in range(n):
    print("%d"%arr[i])
mergeSort(arr,0,n-1)
print("Sorted array is")
for i in range(n):
    print("%d"%arr[i])
