'''like merge sort quicksort is a divide
conquer problem,it picks an elament as pivot element
and partitions the given array around the picked pivot
Different version of pivot:
1.always pick the first element as pivot
2.always pick the last element as pivot
3.pick a random element as pivot
4.pick median as pivot

'''
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def QuickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
#Driver code to test above

arr=[10,7,8,9,1,5]
n=len(arr)
QuickSort(arr,0,n-1)
print("Sorted array is")
for i in range(n):
    print("%d"%arr[i])


