# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:48:16 2024

@author: yan10
"""
# 參考 https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-%E5%84%AA%E5%8C%96%E7%AE%97%E6%B3%95/01-%E5%82%B3%E7%B5%B1%E5%84%AA%E5%8C%96%E6%96%B9%E6%B3%95/01-%E5%84%AA%E5%8C%96/01-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95/03-%E9%80%9A%E7%94%A8%E7%9A%84%E7%88%AC%E5%B1%B1%E6%A1%86%E6%9E%B6/tsp.py
import random
citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

def distance(p1, p2):
    ## print('p1=', p1)
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
        # dist += distance(citys[i], citys[p[i]])
    return dist

#path = [i for i in range(len(citys))]
l = len(citys)
path = [(i+1)%l for i in range(l)]
print(path)
print('pathLength=', pathLength(path))



def neighbor(p):
    p2 = p.copy()
    ran = len(p2)
    city1 = random.randint(0, ran-1)
    city2 = random.randint(0, ran-1)
    temp = p2[city1]
    p2[city1] = p2[city2]
    p2[city2] = temp
    ##print(p2)
    return p2
    
    

def hillClimbing(x,pathLength, neighbor,max_fail=10000):
    fail = 0
    while True:
        nx = neighbor(x)
        if pathLength(nx) < pathLength(x) and pathLength(nx) != 0:
            x = nx
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return x
result = pathLength(hillClimbing(path,pathLength,neighbor))
print('path=',hillClimbing(path,pathLength,neighbor))
print('pathLength=', result)




