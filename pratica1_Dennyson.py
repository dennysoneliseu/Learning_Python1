#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:28:06 2017

@author: labsim
"""
import numpy as np
import matplotlib.pyplot as plt

i1,i2 = 0.8, 0.3

theta = np.linspace(-10,10,1000)

L11 = (3+np.cos(2*theta))*10e-3
L22 = 0.3*np.cos(theta)
L12 = (30+10*np.cos(2*theta))

W = 0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2

T_total = np.diff(W)

W_r = 0.5*L11*i1**2 + 0.5*L22*i2**2
W_m = L12*i1*i2 

T_r = np.diff(W_r)
T_m = np.diff(W_m)

plt.figure(1,[10,7])
plt.subplot(311)
plt.title("Torque Total")
plt.ylabel("Torque em [N*m]")
plt.grid() 
plt.plot(theta[0:len(theta)-1], T_total, 'r')
plt.subplot(312)
plt.title("Torque de relutancia")
plt.ylabel("Torque em [N*m]")
plt.grid()
plt.plot(theta[0:len(theta)-1], T_r)
plt.subplot(313)
plt.title("Torque mutuo")
plt.ylabel("Torque em [N*m]")
plt.xlabel("$\Theta$ em rad")
plt.grid()
plt.plot(theta[0:len(theta)-1], T_m, 'g')
plt.tight_layout()
plt.show()
