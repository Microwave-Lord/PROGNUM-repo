#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
#calculating julian date LMAOOO
D = float(input("What day?"))
M = int(input("What month (use numbers please!"))
Y = int(input("What year?"))

if 1 <= M <= 12 and -5954 < Y:
    JD = 367*Y -7*(Y+(M+9)//12)/4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
    print(f"{JD} is the julian date!")

else:
    print("not a valid result!")

