def shellSort(arr):
    #start with a big gap then reduce the gap
    n=len(arr)
    gap=n//2
    #Do a gapped insertion sort for this gap size
    #the first gap elements a[0..gap-1] are already in gapped
    #order keep adding one or more element until the entire array
    #is gap sorted
    while gap>0:
        for i in range(gap,n):
            #adda a[i] the elements that have been soted
            #save a[i] in tenp and make a hole at position i
            temp=arr[i]
            #shift earlier gap-sorted elements up until the correct
            #liocation a[i] is found
            j=i
            while j>=gap and  arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp

            gap/=2
    for i in arr:
        print(i,end=" ")

arr=[3,43,5,2,5,6,2,56,75]
shellSort(arr)
