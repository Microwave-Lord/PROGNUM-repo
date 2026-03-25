#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math as m
import numpy as np

class Fibonacci:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    def nth(self):
        a = 0
        b = 1
        for i in range (2, (self.n)):
            c = a + b
            a = b
            b = c
        return b
    def fibo(self):
        fiblist = []
        a = 0
        b = 1
        l = 2
        while l<(self.n)-1:
            c = a+b
            a = b
            b = c
            if a%(self.m) == 0:
                fiblist.append(a)
            l = l+1
        return fiblist
    
    
fib = Fibonacci(100, 7)
print(fib.nth())
print(fib.fibo())

