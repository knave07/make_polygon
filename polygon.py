
import matplotlib.pyplot as plt
import random
import numpy as np
n = input("give no. of vertex in polygon")
l1 = random.sample(range(1,100),int(n)) 
l2 = random.sample(range(1,100),int(n))
l3 = []
x = 0
y = 0
for i in range(0,int(n)):
	l3.append((l1[i],l2[i]))
	x+=l1[i]
	y+=l2[i]

x = x/int(n)
y = y/int(n)	
def angle(q):
	a,b = q
	return  np.rad2deg(np.arctan2(b - y, a- x))

l3.sort(key = angle)
print(l3)
for i in range(0,int(n)-1):
	x1,y1 = l3[i]
	x2,y2 = l3[i+1]
	plt.plot([x1,x2],[y1,y2],marker = 'o',color = 'black')

x1,y1 = l3[int(n)-1]
x2,y2 = l3[0]
	
plt.plot([x1,x2],[y1,y2],marker = 'o',color = 'black')
plt.show()
polygon.py
Displaying polygon.py.
