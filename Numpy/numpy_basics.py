import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))
# print(a.shape)

# b = np.array([[1],[2],[3],[4],[5]])
# print(b)
# print(b.shape)

# c = np.array([[1,2,3],[4,5,6]])
# print(c.shape)
# print(c[1][1])
# print(c)

#Array of Zeroes
# a = np.zeros((3,3))
# print(a)

# Array of ones
# b = np.ones((2,3))
# print(b)

#Array of Constants
# c = np.full((3,2),'c')
# print(c)

# Identity Matrix
# d = np.eye(4)
# print(d)

# Random matrix
# random = np.random.random((2,3))
# print(random)
# print(random[:,1])
# print(random[1,1:3])

# z = np.zeros((3,3),dtype = np.int64)
# print(z)
# z[1,:] = 5
# z[:,-1] = 7
# print(z)

# print(z.dtype)


# Mathematical Operations
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

# print(x+y)
# print(np.add(x,y))
# print(x-y)
# print(np.subtract(x,y))
# print(x*y)
# print(np.multiply(x,y))
# print(x/y)
# print(np.divide(x,y))

# Matrix Multiplication / Dot Products

# print(x)
# print(y)
# print(x.dot(y))
# print(np.dot(x,y))

# Multiplication of Vectors
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
# print(a.dot(b))

# print(a)
# print(sum(a))

# print(x)
# print(np.sum(x))
# print(np.sum(x,axis = 0))

# Stacking of Arrays
# print(a)
b = b**2
# print(b)

a = np.stack((a,b),axis = 0)
# print(np.stack((a,b),axis = 1))

#Reshape a Numpy Array
print(a)
a = a.reshape((4,2))
print(a)