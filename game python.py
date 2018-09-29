a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
   25,26,27,28,29,30,31]
b=[]
c=[]
d=[]
e=[]
f=[]
for i in a:
    string=str(bin(i)[2:].zfill(8))
    if string[len(string)-1]=='1':
        b.append(i)
    if string[len(string)-2]=='1':
        c.append(i)
    if string[len(string)-3]=='1':
        d.append(i)
    if string[len(string)-4]=='1':
        e.append(i)
    if string[len(string)-5]=='1':
        f.append(i)
k=0
print(b,end='\n')
a=str(input("is your bday no in this list is yes press y or no n"))
if a=='y' or a=='Y' or a=='yes' or a=='YES':
    k=k+2**0
print(c,end='\n')
b=str(input("is your bday no in this list is yes press y or no n"))
if b=='y' or b=='Y' or b=='yes' or b=='YES':
    k=k+2**1
print(d,end='\n')
c=str(input("is your bday no in this list is yes press y or no n"))
if c=='y' or c=='Y' or c=='yes' or c=='YES':
    k=k+2**2
print(e,end='\n')
d=str(input("is your bday no in this linst is yes press y or no n"))
if d=='y' or d=='Y' or d=='yes' or d=='YES':
    k=k+2**3
print(f,end='\n')
e=str(input("is your bday no in this list is yes press y or no n"))
if e=='y' or e=='Y' or e=='yes' or e=='YES':
    k=k+2**4

print("***your bday date is**** {0}".format(k))


#ecval funnction automatically checks what is the input value