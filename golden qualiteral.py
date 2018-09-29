import math
from math import radians
latdelhi=28.7041
longdelhi=77.1025
latahemdabed=23.0225
longahemdabed= 72.5714
latchennai=13.0827
longchennai=80.2707
latkolkata=22.5726
longkolkata=88.3639
radius=6371
a=radius*math.acos(math.sin(radians(latdelhi))*math.sin(radians(latahemdabed))+math.cos(radians(latdelhi))*math.cos(radians(latahemdabed))*math.cos(radians(longdelhi-longahemdabed)))
b=radius*math.acos(math.sin(radians(latahemdabed))*math.sin(radians(latchennai))+math.cos(radians(latahemdabed))*math.cos(radians(latchennai))*math.cos(radians(longahemdabed-longchennai)))
c=radius*math.acos(math.sin(radians(latchennai))*math.sin(radians(latkolkata))+math.cos(radians(latchennai))*math.cos(radians(latkolkata))*math.cos(radians(longchennai-longkolkata)))
d=radius*math.acos(math.sin(radians(latkolkata))*math.sin(radians(latdelhi))+math.cos(radians(latkolkata))*math.cos(radians(latdelhi))*math.cos(radians(longkolkata-longdelhi)))
e=radius*math.acos(math.sin(radians(latdelhi))*math.sin(radians(latchennai))+math.cos(radians(latdelhi))*math.cos(radians(latchennai))*math.cos(radians(longdelhi-longchennai)))
k=(a+b+e)/2
l=(c+d+e)/2
print(math.sqrt(k*(k-a)*(k-b)*(k-e))+math.sqrt(l*(l-c)*(l-d)*(l-e)))