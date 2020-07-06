# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:47:59 2020

@author: Nadine Snijders
"""

import numpy as np 
import matplotlib.pylab as plt
import control 

#Openlus
teller = np.array([4.0])
noemer = np.array([1.0,4.0])
H      = control.tf(teller, noemer)
print (H)

pole = H.pole()
zero = H.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)

#Gesloten lus 
Kd = 1

Sys1 = Kd*H
Sys2= 1 

Hclosed = control.feedback(Sys1,Sys2)
print (Hclosed)

pole = Hclosed.pole()
zero = Hclosed.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)
#stap respontie openlus

t,y = control.step_response(Hclosed)
t,y = control.step_response(Hclosed,t) 

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()

