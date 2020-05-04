# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:44:58 2020

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

Hjw      = []
absoluut = []
angles   = []
degrees  = []
for w in range (0,5,1):
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
    




