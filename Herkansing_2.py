# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:59:49 2020

@author: Nadine Snijders
"""

import numpy as np 
import matplotlib.pylab as plt
import control.matlab as cm 
import control 

#Openlus
teller = np.array([6.0])
noemer = np.array([1.0,0.4,12])
H      = control.tf(teller, noemer)
print (H)

pole = H.pole()
zero = H.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)

#Gesloten lus 
K = 10

Sys1 = K * H
Sys2= 1 

Hclosed = control.feedback(Sys1,Sys2)
tc,yc = control.step_response(Hclosed)
tc,yc = control.step_response(Hclosed,tc) 

info = cm.stepinfo(Hclosed)
print (info)

plt.plot(tc,yc)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()

#stap respontie openlus
t,y = control.step_response(H)
t,y = control.step_response(H,t) 
print (info)

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()
