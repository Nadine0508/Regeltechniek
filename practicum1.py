# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:45:10 2020

@author: Nadine Snijders 
"""

import numpy as np 
import matplotlib.pylab as plt
import control 

#Openlus
teller = np.array([2.0])
noemer = np.array([1.0,-3.0,])
H      = control.tf(teller, noemer)
print (H)

pole = H.pole()
zero = H.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)

#Gesloten lus 
K = 0.1

teller_k = np.array([2.0*K])
noemer_k = np.array([1.0,-3.0 + K])
H_k      = control.tf(teller_k, noemer_k)
print (H_k)

pole_k = H_k.pole()
zero_k = H_k.zero()

print ("Pool: ",pole_k)
print ("Zero's: ",zero_k)

Sys1 = K*H
Sys2= 1 

Hclosed = control.feedback(Sys1,Sys2)

#stap respontie openlus

#y,t = control.step(H)
#t = np.linspace(0,10,200)
#y = control.step(H,t)[0]

t,y = control.step_response(Hclosed)
t,y = control.step_response(Hclosed,t) 

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()

