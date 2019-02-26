##############################################################################
### You do not need to specify variable type, python does that on its own  ###
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

### Order matters ###
d, c = add_and_sub_two_nums(a, b)
print(c, d)

### You can also have all the returns go to one var ###
c = add_and_sub_two_nums(a, b)
print(c, c[0], c[1])

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

### If else ###
if(a == 10):
    print('a == 10')
else:
    print('a != 10')

### If, else if, else ###  
if(a == 10):
    print('a == 10')
elif(a == 1):
    print('a == 1')
else:
    print('a != 1 or 10')

### While Loop ###
count = 0
while(count < 3):
    print('While: ', count)
    count = count + 1
    
### For loop ###
a = ['cat', 'dog', 'horse']
for i in a:
    print('For: ', i)
    
for i in range(len(a)):
    print('For: ', i)
    
for i in range(len(a)):
    print('For: ', a[i])
    
print('---------------------------------------------------------------------')
  



















