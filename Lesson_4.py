##############################################################################
############################## Import Libraries ##############################
##############################################################################
import os
import csv

##############################################################################
### Save to file as ascci                                                  ###
##############################################################################
filename = 'trash_file.txt'

### Open file as write ###
with open(filename,'w') as file:
    file.write('Hello World!')
    
### It can also be done like this but will need to be closed manually ###
file = open(filename,'w')
file.write('Hello World!')
file.close()

### Notice that the file does not append but overwrites ###
### This will append instead ###
file = open(filename,'a')
file.write('\nHello World!\n') ### \n adds a new line to the write
file.write('Hello World!\n')
file.write('Hello World!\n')
file.write('Hello World!\n')
file.write('Hello World!\n')
file.close()

### Remove trash_file.txt ###
### Be very careful when automating file removal!!!!! ###
os.remove(filename)


##############################################################################
### Save list to file as ascci                                             ###
##############################################################################
filename = 'trash_file.txt'

### List to be saved ###
a = [[1,2,3,4,5],
     [11,22,33,44,55],
     [9,8,7,6,5],
     [13,24,35,46,57],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [0,9,8,7,6,5,4,3,2,1]]

### Save to file with comma delimiter ###
delimiter = ','
file = open(filename, 'w')
for row in a:
    for val in row:
        if(val != row[-1]):
            val_to_write = str(val) + delimiter   ### add delimiter
        else:
            val_to_write = str(val)
        file.write(val_to_write)
    file.write('\n')                              ### add end line
file.close()

### Remove trash_file.txt ###
os.remove(filename)


### You can also use pre built libraries to make this easier ###
file = open(filename, 'w')
file_writer = csv.writer(file, delimiter=",")
file_writer.writerows(a)
file.close() 


##############################################################################
### Read list from file as ascci                                           ###
##############################################################################
### now we are going to read our trash_file.txt ###
file = open(filename, 'r')
file_reader = csv.reader(file, delimiter=",")
for rows in file_reader:
    print(rows)
file.close()


### now we store them in an array as ints ###
file = open(filename, 'r')
file_reader = csv.reader(file, delimiter=",")
b = []
for rows in file_reader:
    if(rows != []):
        b.append([])
        for i in rows:
            b[-1].append(float(i))
file.close()
for row in b:
    print(row)












