#python program for implementation of radix sort
#A function to do counting sort of arr[]
#accoriding to  the digit represented by exp
def countingsort(arr,exp1):
    n=len(arr)
    #the output array
    output=[0]*(n)
    #initialize the countn array as 0
    count=[0]*(10)
    #store count of occurances in count[]
    for i in range(0,n):
        index=(arr[i]/exp1)
        count[int((index)%10)]+=1
    #changeg count i so that actual
    #position of this digit in output array
    for i in range(1,10):
        count[i]+=count[i-1]
    #building the output array
    i=n-1
    while i>=0:
        index=(arr[i]/exp1)
        output[count[int(index%10)]-1]=arr[i]
        count[int((index)%10)]-=1
        i-=1
    #copying the output array to arr
    #so that arr now contains sorted numbers
    for i in range(0,len(arr)):
        arr[i]=output[i]
#Method to do find radix sort
def radixSort(arr):
    #find the maximum number to know the number of digits
    max1=max(arr)
    #Do counting sort for every digit .Note that instead
    #of passing digit number,exp is passed,exp is 10^i
    #where i is the current digit number
    exp=1
    while max1/exp>0:
        countingsort(arr,exp)
        exp*=10
#Driver code to test above
arr=[170,45,75,90,802,24,2,66]
radixSort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')




