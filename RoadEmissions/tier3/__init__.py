# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 20:58:19 2014

@author: tlev
"""

"""
Matematical emission fuctions without parmeters, the function reference
nubers are accoring to the EEA 2013 Guidebook 
"""
from math import exp

def f25(V, a,b,c,d,e):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)   
    EF = (a + c * V + e * V**2)/(1 + b * V + d * V**2)
    return EF

def f26(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a * V**5 + b * V**4 + c * V**3 + d * V**2 + e * V + f
    return EF

def f27(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (a + c * V + e * V**2 + f / V )/(1 + b * V + d * V**2)
    return EF
    
def f28(V, a,b,c,d):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    EF = a * V**b + c * V**d
    return EF
    
    
def f901(V):
    V = float(V)
    EF = 17.5E-3 + 86.42(1+exp(V+117.67/-21.99))**-1
    return EF  