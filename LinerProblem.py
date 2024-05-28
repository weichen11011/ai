import pulp
import pandas

myprolp = pulp.LpProblem('ans', sense=pulp.LpMaximize)

x =pulp.LpVariable('x')
y =pulp.LpVariable('y')
z =pulp.LpVariable('z')
myprolp += 3*x +2*y + 5*z 

# 條件式
myprolp += (x+y <=10)
myprolp += (2*x+z <=9)
myprolp += (y+2*z<=11)
myprolp += (x>=0)
myprolp += (y>=0)
myprolp += (z>=0)

myprolp.solve()

#print("Status:", myprolp.status)

for i in myprolp.variables():
    print(i.name, "=", i.varValue)



  