# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:03:54 2020

@author: Nadine Snijders
"""

import numpy as np
import matplotlib.pylab as plt 
import control 


# 5/s+5

teller = np.array([5.0])
noemer = np.array([1.0,5.0])
H      = control.tf(teller, noemer)
W = [0,10/(2*np.pi),100/(2*np.pi)]
absoluut = [1.0,0.447,0.0499]
degrees  = [0,-63.43,-87.13]


#Bode plot
control.bode(H)
mag,phase,omega = control.bode(H)

for w in range (0,3,1):
    Hw     = control.evalfr(H,1j*W[w])
        # Vul een list met waarde 
    #plt.plot(W[w],absoluut[w],"ro")
    plt.plot(W[w],degrees[w],"ro")

plt.show()
