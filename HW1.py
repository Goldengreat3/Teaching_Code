##############################################################################
############################## Import Libraries ##############################
##############################################################################
import numpy as np

##############################################################################
### Make a function that takes 2 2D arrays and returns the product of 
### these vectors. This function assumes that the arrays are numpy arrays
### and that the second array needs to be transposed for the dot product
##############################################################################
def dot_product(v1, v2):
    v2 = v2.T
    
    n = len(v1)
    m = len(v1[0])
    v3 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            for q in range(m):
                v3[i][j] += v1[i][q]*v2[q][j]
    return v3

##############################################################################
############################## Test the function #############################
##############################################################################
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[4,1],[5,3],[8,1]])

c_np = np.dot(a, b.T)
c_me = dot_product(a, b)

print(c_np)
print(c_me)
print('------------------')

a = np.array([[1, -4,  3,  7,  3,  9],
              [3,  5,  4,  6, -9,  1],
              [5,  6, -9,  9,  7,  1],
              [4,  1,  2,  1,  2,  5],
              [3, -6,  7,  2,  4,  9],
              [8,  0,  3,  5,  6,  7]])
b = np.array([[2, -8,  4, -3,  8,  9],
              [6,  2, -3,  5,  6, -7],
              [4,  4,  1,  6,  4,  4],
              [2, -5,  8, -3,  2, -2],
              [9, -7,  4,  7,  8,  4],
              [3,  9,  6,  9, -4,  8]])
    
c_np = np.dot(a, b.T)
c_me = dot_product(a, b)

print(c_np)
print(c_me)
print('------------------')


a = np.array([[3,1,6,8,3]])
b = np.array([[9,5,2,5,8]])

c_np = np.dot(a, b.T)
c_me = dot_product(a, b)

print(c_np)
print(c_me)
print('------------------')
