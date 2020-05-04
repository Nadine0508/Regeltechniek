# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:27:25 2020

@author: Nadine Snijders 
"""

import numpy as np 
import matplotlib.pylab as plt
import control.matlab as cm 
import control 

#Openlus
teller = np.array([18.0])
noemer = np.array([1.0,1.2,36])
H      = control.tf(teller, noemer)
print (H)

pole = H.pole()
zero = H.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)

#Gesloten lus 
K = 100

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

#Hclosed = control.feedback(Sys1,Sys2)
#tc,yc = control.step_response(Hclosed)
#tc,yc = control.step_response(Hclosed,tc) 
#
#info = cm.stepinfo(Hclosed)
#print (info)
#
#plt.plot(tc,yc)
#plt.ylabel('stap respontie')
#plt.xlabel('Tijd [s]')
#plt.legend('gesloten lus')
#plt.show()

#stap respontie openlus
t,y = control.step_response(H)
t,y = control.step_response(H,t) 

info = cm.stepinfo(H)
print (info)

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()
