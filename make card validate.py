def validateCard(d):
    l = 0
    k = (d)
    for i in range(0, len(k)):
        if i % 2 == 0:
            p = int(k[i]) * 2
            if p > 9:
                p = p - 9
        else:
            p = int(k[i])

        l = l + p

    c=l%10
    for i in range(2,len(k)):
        if i%2 !=0:
            if int(k[i])>c:
                k[i]=str(int(k[i])-c)
                c=0
            else:
                k[i]='0'
                c=c-int(k[i])

    print("The valid card is",k)









print("Enter random nuber")
k=str(input())
validateCard(k)
