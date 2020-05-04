# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:09:17 2020

@author: Nadine Snijders
"""

import numpy as np
import matplotlib.pylab as plt 
import control 


# 5/s+5

teller = np.array([5.0])
noemer = np.array([1.0,5.0])
H      = control.tf(teller, noemer)
W = [0/(2*np.pi),1/(2*np.pi),5/(2*np.pi),10/(2*np.pi),100/(2*np.pi)]
absoluut = [1.0,0.98,0.71,0.45,0.05]
degrees  = [0,-11.3,-45,-63.4,-87.1]


#Bode plot
control.bode(H)
mag,phase,omega = control.bode(H)


for w in range (0,5,1):
    Hw     = control.evalfr(H,1j*W[w])
        # Vul een list met waarde 
    #plt.plot(W[w],absoluut[w],"ro")
    plt.plot(W[w],degrees[w],"ro")


plt.show()





