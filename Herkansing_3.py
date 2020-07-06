# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:02:35 2020

@author: Nadine Snijders
"""

import numpy as np
import matplotlib.pylab as plt 
import control 
import control.matlab as cm 

# 5/s+5

teller = np.array([5.0])
noemer = np.array([1.0,5.0])
H      = control.tf(teller, noemer)
W = [0,10,100]

Hjw      = []
absoluut = []
angles   = []
degrees  = []
for w in range (0,3,1):
    Hw     = control.evalfr(H,1j*W[w])
        # Vul een list met waarde 
    Hjw.append(Hw)
    absoluut.append(np.abs(Hw))
    angles.append(np.angle(Hw))
    degrees.append(np.angle(Hw,deg=True))   

#tabel van maken    
print (H)  
print ("\n")  
print (Hjw)
print ("\n")  
print (absoluut)
print ("\n")  
print (angles)
print ("\n")  
print (degrees)
print ("\n")  