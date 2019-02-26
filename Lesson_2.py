##############################################################################
############################## Import Libraries ##############################
##############################################################################
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
### Show off lists                                                         ###
##############################################################################
a = [1,2,3,4,5,6,7,8,9]  # This is a list
print(a)                 # Print a
print(a[:3])             # print the first three values
print(a[3:])             # print all but the first three values
print(a[-1])             # Print the last value
print(a[::2])            # Print every other value

a = [1, 2.0, '3']        # List values can be of any type
print(a)

a = [[1,2,3],            # They can have lists in them
     ['cat', 'dog', 'horse'],
     [True, False, True]]
print(a)
print('---------------------------------------------------------------------')
##############################################################################
### Show numpy arrays                                                      ###
##############################################################################
a = np.array([1,2,3,4,5,6,7,8,9])         # This is a numpy array
print(a)                                  # Print a
print(a[:3])                              # print the first three values
print(a[3:])                              # print all but the first three values
print(a[-1])                              # Print the last value
print(a[::2])                             # Print every other value

a = np.array([[0,2,3,4,5,6,7,8,9],        # This is a 2D numpy array
              [1,0,3,4,5,6,7,8,9],
              [1,2,0,4,5,6,7,8,9],
              [1,2,3,0,5,6,7,8,9],
              [1,2,3,4,0,6,7,8,9],
              [1,2,3,4,5,0,7,8,9],
              [1,2,3,4,5,6,0,8,9],
              [1,2,3,4,5,6,7,0,9],
              [1,2,3,4,5,6,7,8,0]])
print(a[:,0])                             # Print the first column
print(a[0,:])                             # Print the first row

### modify numpy array ###
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a + 1)                              # Add 1 to each index
print(a - 1)                              # Subtract 1 to each index
print(a * 2)                              # Multiple each index by 2
print(a / 5)                              # divide each index by 5

### Call numpy functions ###
a_sum = np.sum(a)                         # Take the total sum
a_var = np.var(a)                         # Take the total var
a_std = np.std(a)                         # Take the total std

print(a_sum)
print(a_var)
print(a_std)

a_sum = np.sum(a,axis=0)                  # Take the sum over axis 0
a_var = np.var(a,axis=0)                  # Take the var over axis 0
a_std = np.std(a,axis=0)                  # Take the std over axis 0

print(a_sum)
print(a_var)
print(a_std)

### Multiple arrays ###
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[3,2,1],[6,5,4],[9,8,7]])
c = np.dot(a,b)                           # Take the dot product
print(c)









