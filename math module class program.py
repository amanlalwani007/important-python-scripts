import math
x1=2
x2=4
y1=3
y2=4
x3=0
y3=0
a=math.sqrt((x2-x3)**2+(y2-y3)**2)
b=math.sqrt((x1-x3)**2+(y1-y3)**2)
c=math.sqrt((x2-x1)**2+(y2-y1)**2)
A=math.acos((a*a-b*b-c*c)/(-2*b*c))
B=math.acos((b*b-a*a-c*c)/(-2*a*c))
C=math.acos((c*c-b*b-a*a)/(-2*a*b))
print(round(math.degrees(A),2))
print(round(math.degrees(B),2))
print(round(math.degrees(C),2))
