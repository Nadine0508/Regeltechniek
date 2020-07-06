# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:05:06 2020

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
w = 10

#controle van magnitude 
t = np.arange(0,5,0.005)
u = np.sin(2* np.pi * w * t)

plt.plot(t,u)

y,t,x = cm.lsim(H,u,t)
y = cm.lsim(H,u,t)[0]

plt.plot(t,y)
#plt.plot(t,x)


