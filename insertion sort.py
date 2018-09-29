def insertionsort(arr):
   if len(arr)==1:
     print("already sorted",arr)
     return
   else:
     for i in range(1,len(arr)):
         key=arr[i]
         j=i-1
         while j>=0 and arr[j]>key:
             arr[j+1]=arr[j]
             j=j-1
         arr[j+1]=key

     print("sorted array is",arr)
   return


#cards game



arr=[]
print("Enter size of array")
n=int(input())
print("enter elements")
for i in range(0,n):
   k=int(input())
   arr.append(k)
insertionsort(arr)