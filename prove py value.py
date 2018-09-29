import random
circle_inside=0
for i in range(0,100000):
    x=random.random()*2-1
    y=random.random()*2-1
    orig_dist=x*x+y*y
    if orig_dist<=1:
        circle_inside=circle_inside+1

pi=4*(circle_inside/100000)
print('the value of pi is',pi)

