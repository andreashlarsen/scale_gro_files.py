##########################################
# program scales coordinates of gro file
##########################################
import numpy as np

filename_in = input('enter name of input .gro file:  ')
filename_out = input('enter name of output .gro file:  ')
scale_x = float(input('enter scale factor x:  '))
scale_y = float(input('enter scale factor y:  '))
scale_z = float(input('enter scale factor z:  '))
print('\n----------------------------')
print('input file: %s' % filename_in)
print('output file: %s' % filename_out)
print('scaling factor x: %2.2f' % scale_x)
print('scaling factor y: %2.2f' % scale_y)
print('scaling factor z: %2.2f' % scale_z)

f_in = open(filename_in,'r')
f_out = open(filename_out,'w')

line = f_in.readline()
while line:
    #print(line)
    line_split = line.split()
    n = len(line_split)
    if n in [3,5,6,7]:
        idx = n-3
        x,y,z = float(line_split[idx]),float(line_split[idx+1]),float(line_split[idx+2])
        x_scale,y_scale,z_scale = x*scale_x,y*scale_y,z*scale_z
        if n == 3:
            new_line = '%10.5f%10.5f%10.5f\n' % (x_scale,y_scale,z_scale)
        else:
            new_line = '%s%8.3f%8.3f%8.3f\n' %  (line[0:20],x_scale,y_scale,z_scale)
    else:
        new_line = line
    #print(new_line)
    f_out.write(new_line)
    line = f_in.readline()
f_in.close()
f_out.close()
