#the best aalgorithm to find prime numbers between particular range
#is Sieve of Eratosthenes
import time
def SieveOfEratosthenes(n):
 g=time.time()
#creates an boolean array "prime[0..n]" and initialize
#all entries it as true,A value in prime[i] will
#finally be false if i is not a prime,eelse true
 prime=[True for i in range(n+1)]
 p=2
 while(p*p<=n):
    if(prime[p]==True):
    #update all multiplies of p
        for i in range(p*2,n+1,p):
            prime[i]=False
    p=p+1
 #print all prime numbers
 for p in range(2,n):
     if prime[p]:
         print(p)
 j=time.time()
 print(j-g)






if __name__=='__main__':
    n=10000
    print('the prime numbers which are equal or lesser than',n)
    SieveOfEratosthenes(n)
