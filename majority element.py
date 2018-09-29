a=[]
b={}
print("enter size of array")
n=int(input())
for i in range(0,n):
    c=int(input())
    a.append(c)

for i in a:
    b[i]=0

for i in a:
    b[i]=b[i]+1
for i in b:
    if b[i]>(n/2):
        print('the majority element is',i)
        break



