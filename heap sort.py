#python profram implementation of heap sort
#to heapify subtree rooted at index i
#n is the size of the heap
def heapify(arr,n,i):
    largest=i#initialize largest as root
    l=2*i
    r=2*i+1
    #see if left child of root exists and
    #is greater than root
    if l<n and arr[i]<arr[l]:
        largest=l
    #see if right child exists and is
    #greatet than root
    if r<n and arr[largest]<arr[r]:
        largest=r
    #change root is needed
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]#swap
        #hepift the root
        heapify(arr,n,largest)
def heapsort(arr):
    n=len(arr)
    #build a maxheap
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    #one by one extract elements
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
#Driver code test above
arr=[12,11,13,5,6,7]
heapsort(arr)
n=len(arr)
print('Sorted array is')
for i in range(n):
    print(arr[i],end=' ')




