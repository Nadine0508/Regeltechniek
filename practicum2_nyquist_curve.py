# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:58:07 2020

@author: Nadine Snijders
"""

from tabulate import tabulate
import numpy as np
import matplotlib.pylab as plt 
import control 
import control.matlab as cm 

# 5/s+5

teller = np.array([5.0])
noemer = np.array([1.0,5.0])
H      = control.tf(teller, noemer)
W = [0,1,5,10,100]
Hjw      = [[1,0],[0.962,-0.192],[0.5,-0.5],[0.2,-0.4],[0.002,-0.05]]

for w in range (0,5,1):
    Hw     = control.evalfr(H,1j*W[w])
    # Vul een list met waarde 
    Hjw.append(Hw)
    plt.plot(Hjw[w][0],Hjw[w][1],"ro")

print (Hjw)
#Nyquist curve 
control.nyquist(H)
real,img,omega = control.nyquist(H)

plt.plot(Hw,"ro")
plt.figure()
plt.show()