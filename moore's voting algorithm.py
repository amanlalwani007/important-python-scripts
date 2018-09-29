def findCandidate(a,n):
    mjindex=0
    count=1
    for i in range(1,n):
        if a[mjindex]==a[i]:
            count=count+1
        else:
            count=count-1

        if count==0:
            mjindex=i
            count=1
    return a[mjindex]



print("enter size of array")
n=int(input())
a=[]
print('enter array elements')
for i in range(0,n):
    k=int(input())
    a.append(k)
p=findCandidate(a,n)
count=0
for i in a:
    if p==i:
        count=count+1

if count>(n/2):
    print('the majority element is',p)
else:
    print('no majority element')

