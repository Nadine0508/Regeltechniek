# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:28:11 2020

@author: Nadine Snijders
"""


import numpy as np
import matplotlib.pylab as plt 
import control 



#Bode plot 2e graads
Wn = 100
demping = [0.01,0.1,0.2,0.5,1,2]

for d in range(0,6,1):
    teller = np.array([1.0])
    noemer = np.array([(Wn)**-2,((2*demping[d])/Wn),1.0])
    H      = control.tf(teller, noemer)
    print(H)
    mag,phase,omega = control.bode(H)
    plt.plot()
#plt.figure()


