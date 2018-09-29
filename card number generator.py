import random
def check(a):
   l=0
   k=str(a)
   for i in range(0,len(k)):
       if i%2==0:
           p=int(k[i])*2
           if p>9:
                p=p-9
       else:
           p=int(k[i])

       l=l+p
   if l%10==0 and k[0]=='4':
         print('your card is valid and it is visa',a)











for i in range(0,10000):
    a=int(random.uniform(0.4,0.5)*10**16)
    check(a)


