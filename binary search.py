def binarySearch(arr,l,r,x):
    if r>=l:
        mid=(l+(r-1))//2
        #if element is present in the middlel
        if arr[mid]==x:
            return mid
        #if element is smaller than mid
        #can only be present in the left subarray
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        #else the elemrnt can only be present
        #in right subarray
        else:
            return binarySearch(arr,mid+1,r,x)


#test array
arr=[2,3,4,10,40]
x=10
#function call
result=binarySearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element found at",result)
else:
    print("Element is not found in array")

