import numpy as np

#4. Sean A = {a,b,c}, B = {x,y} y C = {0, 1}. Calcular:
a = np.array([1, 2, 3])
b = np.array([2, 3])
c = np.array([0, 1])
axb= np.cross(a, b)
print (np.cross(axb, c))

bxb = (np.cross(b, b))
print (np.cross(bxb, b))
