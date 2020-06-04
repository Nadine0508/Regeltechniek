# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:17:47 2020

@author: Nadine Snijders 
"""

import numpy as np
import matplotlib.pylab as plt 
import control 
import control.matlab as cm 


teller = np.array([-5.0])
noemer = np.array([1.0,0.0])
H      = control.tf(teller, noemer)

print (H)
Kp = 5
Ki = 0.5

teller_s = np.array([1.0])
noemer_s = np.array([1.0,0.0])
s = control.tf(teller_s,noemer_s)

Sys1 = (Kp) * H
Sys2= 1 

Sys1_d = (Kp + Ki* 1/s) * H
Sys2_d= 1 

Hclosed_kp = control.feedback(Sys1,Sys2)
Hclosed_kp_ki = control.feedback(Sys1_d,Sys2_d)

print (Sys1_d)
print (Hclosed_kp_ki)

t,y = control.step_response(Hclosed_kp_ki)
t,y = control.step_response(Hclosed_kp_ki,t) 


mag,phase,omega = control.bode(Hclosed_kp_ki,dB = True)
mag,phase,omega = control.bode(Hclosed_kp_ki,dB = True)
plt.figure()

plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()