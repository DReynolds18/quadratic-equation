# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:43:25 2022

@author: dreynolds18

Find the radius of the circle inside the unit square that has the property
that the average distance of points inside the circle to the center of the 
square  is the same as the average distance of points outside the circle to 
the nearest edge of the square. 
"""

import numpy as np

# ticks = (0.1,0.2,0.3,0.4,0.5)
def finddistance(cords):
     ex = cords[0]
     ey = cords[1]
     d = np.sqrt(((ex)**2)+((ey)**2))
     return d
 
#was in code 
ds = []
for y in np.arange(0,.5, step=.01):
    d = finddistance([.5, y])
    ds.append(d/2)
print(np.mean(ds))

#added values
averagein,averageout= 9,0
d = .2027
passed = 0

while passed != 100:#loop start
    
   xay = np.zeros((100,2))#= [x,y] 
   xay = np.random.uniform(0,0.5,size = (200,2)) #,np.random.uniform(0,0.5,100)
    #print(x,y)
    
   d2center = []
   d2edge = []
   outside = 0
   inside= 0
   for i in range(200):
        #print(np.sqrt(x[i]**2+y[j]**2))
       if np.sqrt(xay[i][0]**2+xay[i][1]**2) <= d  :
            inside+=1
            d2center.append(finddistance(xay[i]))
       else:
            d2edge.append(min(.5-xay[i][0],.5-xay[i][1]))
   print(np.mean(d2center))
   averagein =np.mean(d2center)
   print(np.mean(d2edge))
   averageout =np.mean(d2edge)
   
   if abs(averagein - averageout)< 0.0001:
        passed = 100
        break
   elif averagein< averageout:
        d+=.000001
   elif averagein > averageout:
        d-=.000001
        
   print("shit it failed")
   print(f"d is now {d}")