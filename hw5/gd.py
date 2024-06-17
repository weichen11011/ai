import math
import numpy as np
from numpy.linalg import norm

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, h=0.01):
    p1 = p.copy()
    p1[k] = p[k]+h
    return (f(p1) - f(p)) / h

# 函數 f 在點 p 上的梯度
def grad(f, p, h=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, h)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    print(p)
    for i in range(max_loops):
        fp = f(p)
        fp.backward()
        #gp = grad(f, p) # 計算梯度 gp
        gp = []
        for value in p:
            gp.append(value.grad)
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        if i%dump_period == 0: 
            print("gp=", gp)
        if glen < 0.00001: # 如果步伐已經很小了，那麼就停止吧！
            break
        gh = np.multiply(gp, -1*h) # gh = 逆梯度方向的一小步
        p +=  gh # 向 gh 方向走一小步
    answer=[]
    for k in p:
        answer.append(k.data)
    print(answer)
    return p # 傳回最低點！
