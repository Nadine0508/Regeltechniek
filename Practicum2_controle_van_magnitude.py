# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:14:38 2020

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

#controle van magnitude 
t = np.arange(0,1000,0.1)
u = np.sin(t*5)
#plt.plot(t,u)

y,t,x = cm.lsim(H,u,t)
#y = cm.lsim(H,u,t)[0]
print(y,x,t)

