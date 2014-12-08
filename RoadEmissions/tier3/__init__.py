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
from math import ln


def f25(V, a,b,c,d,e):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)   
    EF = (a + c * V + e * V**2)/(1.0 + b * V + d * V**2)
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
    EF = (a + c * V + e * V**2 + f / V )/(1.0 + b * V + d * V**2)
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

def f30(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (a + c * V + e * V**2)/(1.0 + b * V + d * V**2) + f/V
    return EF
    
def f31(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF =  a + (b / (1+exp((((-1) * c) + (d * ln(V))) + (e * V))))
    return EF

def f36(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a - (b * exp(((-1.0) * c) * (V**d)))
    return EF
    
def f37(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = 1.0 / (((c * (V**2)) + (b * V)) + a)
    return EF

def f38(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (a + (b * V))+(((c - b) * (1-exp(((-1) * d) * V))) / d)    
    return EF

def f39(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (e + (a * exp(((-1) * b) * V))) + (c * exp(((-1) * d) * V))
    return EF

def f40(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a * V**3 + b * V**2 + c * V + d
    return EF

def f41(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = 1.0 / (a + (b * (V**c)))
    return EF

def f42(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = 1.0 / (a + (b * V))
    return EF

def f43(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a * V**2 + b * V + c
    return EF

def f44(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a * b**V * V**c
    return EF

def f45(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = c + (a * exp(((-1) * b) * V))
    return EF

def f46(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = c + (a * exp(b * V))
    return EF

def f47(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = exp( a + (b / V)) + (c * ln(V))
    return EF

def f48(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (a + b * V)-1.0/c
    return EF

def f49(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a + b * V + (c-b) * (1.0 – exp((-1) * V))/d
    return EF

def f50(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = ((e + ( a × exp (((-1) * b ) * V ))) + (c * exp(((-1)* d * V)))
    return EF

def f51(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = (1.0/((( c * ( V**2) + (b * V )) + a ))
    return EF

def f52(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a – (b * exp(((-1) * c ) * ( V**d)))
    return EF

def f53(V,a,b,c,d,e,f):
    #There is an error in this one
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a / (1 + (b * exp(((-1) * c) * )))
    return EF

def f54(V,a,b,c,d,e,f):
    V = float(V)
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)
    EF = a – (b * exp(((-1) * c ) * ( V**d)))
    return EF
