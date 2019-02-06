import numpy as np

a = np.arange(10) + 5
# print(a)

np.random.seed(2)
np.random.shuffle(a)
print(a)

# a = np.random.rand(2,3)
# a = np.random.randn(2,3)
# a = np.random.randint(2,10,5)
# print(a)

# element = np.random.choice([1,4,2,11,56])
# print(element)