#k=int(input("Enter a number"))
import time
p=time.time()

for k in range(1,10000):
    s = int((k / 2) + 1)
    flag = 0
    for i in range(2,s):
        if k%i==0:
            flag=1
            break
    if flag==1:
        print('the number is not prime',k)
    else:
        print('the number is prime',k)
l=time.time()
print(p)
print(l)
print(l-p)