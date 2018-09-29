import random
def check(a):
   l=0
   k=(a)
   for i in range(0,len(k)):
       if i%2==0:
           p=int(k[i])*2
           if p>9:
                p=p-9
       else:
           p=int(k[i])

       l=l+p
   if l%10==0:
       if a[0]=='4':
            print('your card is valid and it is visa',a)
       elif a[0]=='5':
           print('your card is valid and it is master card',a)
       elif a[0]=='6':
           print('your card is valid and it is discover card',a)
       elif a[0:2]=='37':
           print('your card is valid and it is american express card',a)

   else:
       print("card is invalid")
check('4199999999999999')
