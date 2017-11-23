# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:30:24 2017

@author: M K Shrimali
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['xtick.top'] = 'True'
matplotlib.rcParams['ytick.right'] = 'True'
matplotlib.rcParams['grid.linestyle'] = '--'

t=np.linspace(0.,500,1000)
epsilon=0.01
delta=2.

def func(u,t,dlta):
    y,ydot,thta,thtadot=u
    return [ydot,-dlta**2*y+(1+y)*(thtadot)**2-(1-np.cos(thta)),thtadot,(-2*ydot*thtadot-np.sin(thta))/(1+y)]

u0=2.*epsilon*np.array([0,1.,0,1])

sol=odeint(func,u0,t,args=(delta,))

plt.figure()
plt.plot(t,sol[:,0],label=r'${\bf y}(t)$')
#plt.plot(t,sol[:,1],'--',label=r'${\bf \dot{y}}(t)$')
plt.plot(t,sol[:,2],label=r'${\bf\theta}(t)$')
plt.xlabel(r'$t$',fontsize=18)
plt.ylabel(r'$y(t),\theta(t)$')#,\dot{y}(t)$',fontsize=18)
plt.legend(loc=0)
plt.xlim([0.,t.max()])
plt.title(r'$\varepsilon$ = {}   $\delta = {}$'.format(epsilon,delta))
#plt.savefig('P3.png',dpi=1200)

from scipy.signal import hilbert
def envelope(x):
    return {'Upper':np.abs(hilbert(x)), 'Lower':-np.abs(hilbert(-x))}

#up_y=envelopef(sol[:,0])['Upper_Envelope']
#lw_y=envelopef(sol[:,0])['Lower_Envelope']
#up_t=envelopef(sol[:,2])['Upper_Envelope']
#lw_t=envelopef(sol[:,2])['Lower_Envelope']

ye=envelope(sol[:,0])
thtae=envelope(sol[:,2])

up_y=ye['Upper']
up_thta=thtae['Upper']
lw_y=ye['Lower']
lw_thta=thtae['Lower']

#
#plt.figure(1)
#plt.plot(t,up_y,label='Y-Envelope:Upper')
#plt.plot(t,lw_y,label='Y-Envelope:Lower')
#plt.plot(t,up_thta,label=r'$\theta$-Envelope:Upper')
#plt.plot(t,lw_thta,label=r'$\theta$-Envelope:Lower')
#plt.plot(t,up_thta,label=r'$\bf \theta$-Envelope:Upper')
plt.legend(loc=0)
