# Min, Mean, Median, Average, Standard Deviation,
#Variance

import numpy as np

a = np.array([[1,2,3,4],[5,4,1,8]])
# print(np.min(a))
# print(np.min(a,axis = 0))
# print(np.min(a,axis = 1))

# b = np.array([1,2,3,4,5])
# m = sum(b)/5
# print(m)

# print(np.mean(b))
# print(np.mean(a,axis = 0))
# print(np.mean(a,axis = 1))

c = np.array([1,5,4,2,0])
# print(np.median(c))
# print(np.mean(c))

# wt = np.array([1,2,3,4,5])
# print(np.average(c,weights =wt))

# Standard Deviation
u = np.mean(c)
myStd = np.sqrt(np.mean(abs(c-u)**2))
print(myStd)

#Inbuilt
dev = np.std(c)
print(dev)

#Varaince
print(myStd**2)
print(np.var(c))