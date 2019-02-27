##############################################################################
############################## Import Libraries ##############################
##############################################################################
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
### Make a simple plot                                                     ###
##############################################################################
a = [1,2,3,4,5,6,7,8,9]
 
### Create the figure and plot ###
plt.figure()
plt.plot(a)



a = [1,2,3,4,5,6,7,8,9]
b = [9,6,4,1,4,6,8,5,2]

### Create a figure and plot two things ###
plt.figure()
plt.plot(a)          # Plot a
plt.plot(b)          # Plot b on the same figure



x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y = [  1,   3,   7,   2,   8,   1]

### Create a figure and plot one array against the other ###
plt.figure()
plt.plot(x,y)        # plot y against x




##############################################################################
### Make a cool plot                                                       ###
##############################################################################
x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y = [  1,   3,   7,   2,   8,   1]

plt.figure()                        # Create the figure
plt.plot(x,y)                       # Plot y against x
plt.title('Cool Title')             # Set a cool title
plt.xlabel('Time (s)')              # Label the x axis
plt.ylabel('Amplitude (V)')         # Label the y axis
plt.grid(which='major')             # Enable gridlines




##############################################################################
### Make a cool plot with subplots                                         ###
##############################################################################
x  = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y1 = [  1,   3,   7,   2,   8,   1]
y2 = [  4,   2,   5,   8,   2,   9]
y3 = [  7,   5,   2,   6,   5,   3]
y4 = [  5,   8,   0,   1,   0,   6]

plt.figure()                  # Create the figure
plt.subplot(4,1,1)            # Set up subplot 4x1 and this is the first plot
plt.plot(x,y1)                # Plot y1 against x
plt.subplot(4,1,2)            # Set up subplot 4x1 and this is the second plot
plt.plot(x,y2)                # Plot y2 against x
plt.subplot(4,1,3)            # Set up subplot 4x1 and this is the third plot
plt.plot(x,y3)                # Plot y3 against x
plt.subplot(4,1,4)            # Set up subplot 4x1 and this is the fourth plot
plt.plot(x,y4)                # Plot y4 against x

