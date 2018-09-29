import time
k=int(time.time())
while k>(24*60*60):
     k=k-(24*60*60)
c=0
while k>3600:
    k=k-3600
    c=c+1
print('the hous is',c)
print('the seconds is',k/60)


