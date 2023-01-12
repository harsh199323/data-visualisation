

import numpy as np
import matplotlib.pyplot as plt

path='slice150.raw'
#reading raw fine
array=np.fromfile(path, count=-1,dtype='uint16')

#reshaping to 512*512 2D
x=np.reshape(array,(512,512))



#extracting 256th line
xa=x[255]

#a) profile line through line 256 
plt.plot(np.arange(512),xa)
plt.title('Profile Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('profileLine',dpi=150,quality=500)
plt.show()


#b) mean and variance
sum=0
count=0
for ix,iy in np.ndindex(x.shape):
    n=int(x[ix,iy])
    count=count+1
    sum=sum+n
mean=sum/count
print('mean :',mean)
print('variance :',np.var(array))

#949.98 is mean
#134932.47 is variance



#c) histogram of 2D dataset using line-graph
#have used np.unique to count number of times data points have occured
unique,occurence=np.unique([x],return_counts=True)

plt.plot(unique,occurence,'r',linewidth=0.9)
plt.title('Histogram')
plt.xlabel('unique values along X-axis')
plt.ylabel('occurences along Y-axis')
plt.savefig('histogram',dpi=150,quality=500)
plt.show()




#d) linear transformation
smax=255
rmin=np.min(x)
rmax=np.max(x)
s = np.array([])
#normalizing r
s = ((x - rmin)/(rmax - rmin))*smax
s = np.int_(s)

img=plt.imshow(s, cmap='gray')
plt.title('linear Transformation')
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(s),np.max(s)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('linearTransformation',dpi=150,quality=500)
plt.show()





#e) non linear transformation
import math
y=x.reshape(512*512)
sn= np.array([])

#using log2 for transformation
for ele in y:
    sn=np.append(sn,math.log2(ele+1))


#reshaping back to 512*512
sn=sn.reshape(512,512)

img=plt.imshow(sn, cmap='gray')
plt.title('Non-linear Transformation')
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(sn),np.max(sn)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('Non_linear_Transformation',dpi=150,quality=500)
plt.show()





#f) 11*11 boxcar plot
m,n=x.shape
box=[]
rows,cols=512,512

#traversing outter matrix
for i in range(0,rows-10):
    for j in range(0,cols-10):
        #11*11 matrix traverse
        asplit=x[i:(i+11),j:(j+11)]
        #calculating sum of 11*11 matrix
        box=np.append(box,(asplit.sum()/121))
        
#reshaping to 502*502 as corner rows and cols are lost after smoothening
boxOut=box.reshape(502,502)
img=plt.imshow(boxOut,cmap='gray')

plt.title('Box-Car Smoothening')
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(boxOut),np.max(boxOut)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('BoxCar',dpi=150,quality=500)
plt.show()



#g) 11*11 median plot

med=[]
rows,cols=512,512
#traversing outter matrix 512*512
for i in range(0,rows-10):
    for j in range(0,cols-10):
        #traversing 11*11 matrix
        asplit=x[i:(i+11),j:(j+11)]
        #using np.median to get median of 11*11
        med=np.append(med,np.median(asplit))
medOut=med.reshape(502,502)
img=plt.imshow(medOut,cmap='gray')

plt.title('Median Smoothening')
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(medOut),np.max(medOut)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('Median',dpi=150,quality=500)
plt.show()





