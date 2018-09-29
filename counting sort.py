#counting sort is based upon hashing and in this element are not compare with each other
def countingsort(arr):
    max1=0
    for i in arr:
        if i>max1:
            max1=i
    b=[0 for i in range(max1+1)]
    for i in arr:
        b[i]=b[i]+1
    for i in range(1,len(b)):
        b[i]=b[i]+b[i-1]
    c=["" for i in range(len(arr))]
    for j in range(len(arr)-1,-1,-1):
        c[b[arr[j]]-1]=arr[j]
        b[arr[j]]=b[arr[j]]-1
    print('the sorted array is ')
    for i in c:
        print(i,end=' ')

















if __name__=='__main__':
   arr=[3,44,2,2,56,6,88,2,4,6,7,32,5,21]
   countingsort(arr)