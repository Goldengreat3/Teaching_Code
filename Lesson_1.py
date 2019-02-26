##############################################################################
############################## Import Libraries ##############################
##############################################################################
import numpy as np
import matplotlib.pyplot as plt



##############################################################################
### You do not need to specify variable type, python does that on its own ###
##############################################################################
### Vars ###
a = 3
b = 3.0
c = '3'

### Print Var type ###
print('a Type: ', type(a))
print('b Type: ', type(b))
print('c Type: ', type(c))

print('---------------------------------------------------------------------')

##############################################################################
### You can force python to set the variable type if you want              ###
##############################################################################

### Vars ###
a = str(3)
b = int(3.0)
c = float('3')

### Print Var type ###
print('a Type: ', type(a))
print('b Type: ', type(b))
print('c Type: ', type(c))

print('---------------------------------------------------------------------')

##############################################################################
### How to define and call a function                                      ###
##############################################################################
### Function definition ###
def hello_world():
    print('Hello World')
    return

### Call the function ###
hello_world()

### Function definition with input ###
def print_string(to_be_printed):
    print(to_be_printed)
    return

### Call the function ###
to_be_printed = 'Printing!!! :D'
print_string(to_be_printed)

### Function definition with input and output ###
def add_two_nums(a,b):
    c = a + b
    return c

### Call the function ###
a = 3
b = 5
c = add_two_nums(a, b)
print(c)

### Function definition with input and multi output ###
def add_and_sub_two_nums(a,b):
    c = a + b
    d = a - b
    return c, d

### Call the function ###
a = 3
b = 5
c, d = add_and_sub_two_nums(a, b)
print(c, d)

print('---------------------------------------------------------------------')

##############################################################################
### Loops and if statments                                                 ###
##############################################################################
### If statment ###
if(True):
    print('True')
    
a = 1
if(a == 1):
    print('a == 1')
    
if(a != 10):
    print('a != 10')

### While Loop ###
count = 0
while(count < 3):
    print(count)
    
### For loop ###
a = ['cat', 'dog', 'horse']
for i in a:
    print(i)
    
for i in range(len(a)):
    print(i)
    
print('---------------------------------------------------------------------')
  



















