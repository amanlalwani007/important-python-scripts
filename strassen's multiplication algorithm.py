'''Simple way to multiply two matrix
def mulyiply(a[][n],b[][n],c[],[n]):
    for i in range(n):
        for j in range(n):
            c[i][j]=0
            for k in range(n):
                c[i][j]+=a[i][k]*b[k][j]
'''

'''Strassen 's algorithm 
p1=a(f-h)
p2=(a+b)h
p3=(c+d)e
p4=d(g-e)
p5=(a+d)(e+h)
p6=(b-d)(g+h)
p7=(a-c)(e+j)

matrix=[a,b,c,d]*[e,f,g,h]=[p5+p4-p2+p6,p1+p2,p3+p4,p1+p5-p3-p7]
 
'''