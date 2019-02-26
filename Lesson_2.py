##############################################################################
############################## Import Libraries ##############################
##############################################################################
import numpy as np

##############################################################################
### Show off lists                                                         ###
##############################################################################
### Cool stuf you can do with lists ###
a = [1,2,3,4,5,6,7,8,9]          # This is a list
print(a)                         # Print a
print(a[:3])                     # print the first three values
print(a[3:])                     # print all but the first three values
print(a[-1])                     # Print the last value
print(a[::2])                    # Print every other value

### Lists can be different types ###
a = [1, 2.0, '3']                # List values can be of any type
print(a)

### Add two lists (it appends them) ###
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

### Add to a list ###
a = [1,2,3]
print(a)
a.append(4)                      # Append to list
print(a)

### Lists can even be lists of different stuff ###
a = [[1,2,3],                    # They can have lists in them
     ['cat', 'dog', 'horse'],
     [True, False, True]]
print(a)
print('---------------------------------------------------------------------')
##############################################################################
### Show numpy arrays                                                      ###
##############################################################################
### You can do the indexing as lists ###
a = np.array([1,2,3,4,5,6,7,8,9])         # This is a numpy array
print(a)                                  # Print a
print(a[:3])                              # print the first three values
print(a[3:])                              # print all but the first three values
print(a[-1])                              # Print the last value
print(a[::2])                             # Print every other value

### Turn list into numpy array ###
a = [1,2,3]                               # Make a list
print(a)
b = np.array(a)                           # Turn list into a numpy array
print(b)
c = b.tolist()                            # Turn numpy array into a list
print(c)

### Sadly numpy arrays cannot be all different types But there are many    ###
### operations you can do due to them being homogenous                     ###

### You can even do more complicated indexing ###
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

### Adding two numpy arrays ###
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)

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

### Initialize an array of zeros ###
a = np.zeros((4,6))                       # Make a 4x6 array of zeros
print(a)
a = np.ones((4,6))                        # Make a 4x6 array of ones
print(a)






