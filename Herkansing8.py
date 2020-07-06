# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:22:57 2020

@author: snijd
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:59:39 2020

@author: snijd
"""

import numpy as np
import matplotlib.pylab as plt 
import control 
import control.matlab as cm 


teller = np.array([30.0])
noemer = np.array([0.1,1.0])
H      = control.tf(teller, noemer)

print (H)
Kp = 0.5
Ki = 7.5
Kd = 0.005

teller_s = np.array([1.0,0.0])
noemer_s = np.array([1])
s = control.tf(teller_s,noemer_s)

Sys1 =  H
Sys2= 1 

Sys1_d = (Kp + Kd * s + Ki/s) * H
Sys2_d= 1 

Hclosed_kp = control.feedback(Sys1,Sys2)
Hclosed_kp_kd = control.feedback(Sys1_d,Sys2_d)

pole = Hclosed_kp_kd.pole()
zero = Hclosed_kp_kd.zero()

print ("Pool: ",pole)
print ("Zero's: ",zero)
print (Hclosed_kp_kd)


t,y = control.step_response(Hclosed_kp_kd)
t,y = control.step_response(Hclosed_kp_kd,t) 


#mag,phase,omega = control.bode(Hclosed_kp,dB = True)
mag,phase,omega = control.bode(Hclosed_kp_kd ,dB = True)
plt.figure()


plt.plot(t,y)
plt.ylabel('stap respontie')
plt.xlabel('Tijd [s]')
plt.legend('gesloten lus')
plt.show()