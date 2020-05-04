# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:50:54 2020

@author: Nadine Snijders 
"""

import numpy as np
import matplotlib.pylab as plt 
import control 


teller = np.array([1.0])
noemer = np.array([1.0,0.0,0.0])
H      = control.tf(teller, noemer)

print (H)
Kp = 100
Kd = 0.1

teller_s = np.array([1.0,0.0])
noemer_s = np.array([0.0000001])
s = control.tf(teller_s,noemer_s)

print (s)

Sys1 = (Kp + Kd * s) *H
Sys2= 1 

Hclosed = control.feedback(Sys1,Sys2)


t,y = control.step_response(Hclosed)
t,y = control.step_response(Hclosed,t) 

mag,phase,omega = control.bode(H)
plt.figure()

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()