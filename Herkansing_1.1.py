# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:09:05 2020

@author: Nadine Snijders 
"""

import numpy as np 
import matplotlib.pylab as plt
import control 

#Plot clocsed_loop verschillende regelaars
K_c = [-0.1,-1.1,-10]

for c in range (0,3,1):
    teller_kc = np.array([4.0])
    noemer_kc = np.array([1.0,4.0])
    H_kc      = control.tf(teller_kc, noemer_kc)
    print (H_kc)
    
    
    Sys1 = K_c[c]*H_kc
    Sys2= 1 
    
    Hclosed = control.feedback(Sys1,Sys2)
    
    
    t,y = control.step_response(Hclosed)
    t,y = control.step_response(Hclosed,t) 
    
    plt.plot(t,y)
    plt.ylabel('stap respontie')
    plt.xlabel('Tijd [s]')
    plt.legend('gesloten lus')
    plt.show()