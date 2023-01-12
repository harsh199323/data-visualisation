#importing numpy package to load data from field2.irreg.txt
#importing matplotlib package for plotting purposes

import numpy as np
import matplotlib.pyplot as plt

#open file for extraction
filePath='C:/Users/harsh/Desktop/python/IDV/field2.irreg.txt'
openFile = open(filePath,"r")

#extracting data, here I have skipped first 6 lines as it is header part, and 
#further with help of ' '(space delimiter) have etracted data of x,y,zu,v,w. and later got to know z and w had only zeros so 3D plot is impossible and started 2D plot

x,y,z,u,v,w=np.loadtxt(filePath,delimiter=' ',skiprows=6,usecols =(0, 1, 2, 3, 4, 5),unpack = True,)   

#close file after extraction
openFile.close()


#plotting quiver to know the movement of water beacuse of wind
fig, ax = plt.subplots(1,1,figsize = (23,14))
plt.title('Movement of Water Particles')
    
n = -1
color_array = np.sqrt(((v-n)/2)**2 + ((u-n)/2)**2)
Q=ax.quiver(x,y,u,v,color_array,
                scale=20,pivot='tip',units='width',cmap='viridis') 


hbar=plt.colorbar(Q)
hbar.set_ticks([0.5,1.1])
hbar.set_ticklabels(['low','high'])
ax.set_xlabel('X displacement')
ax.set_ylabel('Y displacement')

ax.set_aspect('equal')
plt.savefig('idv_as1.png', dpi=300)  
plt.show()