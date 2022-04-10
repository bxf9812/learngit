#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a = float("inf") #无穷大

w0 = [[0,4,5,a,a],[a,0,3,a,6], [a,a,0,-2,3],[a,1,a,0,a],[-4,a,a,2,0]] #建立网络图形矩阵

length = len(w0)
r0_arr = np.zeros((length,length),dtype = "float32")
w0_arr = np.array(w0)

#算r0_arr
for i in range(length):
    for j in range(length):
        if w0_arr[i][j] == a:
            r0_arr[i][j] = 0
        elif w0_arr[i][j] == 0:
            r0_arr[i][j] = 0
        else:
            r0_arr[i][j] = j + 1

#floyd算法
for k in range(length):
    print("k = {}：".format(k))
    print("w{} = ".format(k))
    print(w0_arr)
    print("r{} = ".format(k))
    print(r0_arr)
    print("\n")
    for i in range(length):
        for j in range(length):
            if w0_arr[i][j] > w0_arr[i][k] + w0_arr[k][j]:
                w0_arr[i][j] = w0_arr[i][k] + w0_arr[k][j]
                r0_arr[i][j] = r0_arr[i][k]

print("k = {}：".format(length))
print("w{} = ".format(length))
print(w0_arr)
print("r{} = ".format(length))
print(r0_arr)
print("\n")   

input("请按Enter键退出：")
# In[7]:


