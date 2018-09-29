import math
def prime(k):
    s=int(math.sqrt(k))
    for i in range(2,s+1):
        if k%i==0:
            return 1
        break

k=int(input("Enter a number"))
p=prime(k)
if p==1:
    print('the number is not prime',k)
else:
    print('the number is prime',k)