import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

path='C:/Users/harsh/Desktop/python/IDV/assignment3/orion/i170b2h0_t0.txt'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, header=None)

#flipping data
df=df.reindex(index=df.index[::-1])

#converting to array
band2=np.asarray(df)

print('Max :',band2.max())
print('Min :',band2.min())
print('Mean :',band2.mean())
print('Variance :',np.var(band2))


#profileline
rowmax,colmax=(np.where(band2[:]==band2.max()))
rowmin,colmin=(np.where(band2[:]==band2.min()))

band2[int(rowmax)][int(colmax)]
profileLine=band2[int(rowmax)].flatten()
img=plt.plot(np.arange(500),profileLine)
plt.title('Profile_line')
plt.xlabel('x-Axes range(0-499)')
plt.ylabel('y-Axes normalized')
plt.yscale('log')
plt.savefig('ProfileLine',dpi=150,quality=500)
plt.show()



#histogram
unique,occurence=np.unique([band2],return_counts=True)

img=plt.plot(unique,occurence,'r',linewidth=0.9)
plt.xscale('log')
plt.title('Histogram')
plt.xlabel('DataSet Values')
plt.ylabel('Occurence Values')
plt.savefig('Histogram',dpi=150,quality=500)
plt.show()



#Histogram-Equalization Using nonLinearTransformation


duplicate=band2.reshape(500*500)
sn= np.array([])

#using log2 for transformation
for ele in duplicate:
    sn=np.append(sn,math.log2(ele+1))

sn=sn.reshape(500,500)

img=plt.imshow(sn, cmap='gray')
plt.title('Non-linear Transformation')
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(sn),np.max(sn)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('Non_linear_Transformation',dpi=150,quality=500)
plt.show()



#AllBands

#Band1

path='C:/Users/harsh/Desktop/python/IDV/assignment3/orion/i170b1h0_t0.txt'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, header=None)

#flipping data
df=df.reindex(index=df.index[::-1])

#converting to array
band1=np.asarray(df)


b1=band1.reshape(500*500)
unique,occurence=np.unique(b1,return_counts=True)
    
list=['r','p','pr','cdf','s']
x=pd.DataFrame(index=unique,columns=list)
    
    
x['r']=unique
x['p']=occurence 
x['pr']=x['p']/len(b1)

a_pr=x['pr'].to_numpy()
a_cdf=x['cdf'].to_numpy()
a_cdf=[sum(a_pr[0:m+1]) for m in range(len(unique))]
x['cdf']=a_cdf

x['s']=x['cdf']*255
    
    
a_s=x['s'].to_numpy()
arr_eq = np.zeros(250000)
    
for i in range(len(unique)):
    ix = np.where(b1 == unique[i])
    ix1 = ix[0]
    arr_eq[ix1] = a_s[i]

#recording for rgbHisto Equalisation 
b_1=arr_eq    
arr_eq2d = arr_eq.reshape(500,500)

img=plt.imshow(arr_eq2d,cmap = 'gray')
plt.title('Histogram Equalization Band1')
plt.grid()
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(arr_eq2d),np.max(arr_eq2d)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('band1',dpi=150,quality=500)
plt.show()


#band2
path='C:/Users/harsh/Desktop/python/IDV/assignment3/orion/i170b2h0_t0.txt'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, header=None)

#flipping data
df=df.reindex(index=df.index[::-1])

#converting to array
band2=np.asarray(df)


b2=band2.reshape(500*500)
unique,occurence=np.unique(b2,return_counts=True)
    
list=['r','p','pr','cdf','s']
x=pd.DataFrame(index=unique,columns=list)
    
    
x['r']=unique
x['p']=occurence 
x['pr']=x['p']/len(b2)

a_pr=x['pr'].to_numpy()
a_cdf=x['cdf'].to_numpy()
a_cdf=[sum(a_pr[0:m+1]) for m in range(len(unique))]
x['cdf']=a_cdf

x['s']=x['cdf']*255
    
    
a_s=x['s'].to_numpy()
arr_eq = np.zeros(250000)
    
for i in range(len(unique)):
    ix = np.where(b2 == unique[i])
    ix1 = ix[0]
    arr_eq[ix1] = a_s[i]
    
arr_eq2d = arr_eq.reshape(500,500)

img=plt.imshow(arr_eq2d,cmap = 'gray')
plt.title('Histogram Equalization Band2')
plt.grid()
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(arr_eq2d),np.max(arr_eq2d)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('band2',dpi=150,quality=500)
plt.show()



#band3
path='C:/Users/harsh/Desktop/python/IDV/assignment3/orion/i170b3h0_t0.txt'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, header=None)

#flipping data
df=df.reindex(index=df.index[::-1])

#converting to array
band3=np.asarray(df)


b3=band3.reshape(500*500)
unique,occurence=np.unique(b3,return_counts=True)
    
list=['r','p','pr','cdf','s']
x=pd.DataFrame(index=unique,columns=list)
    
    
x['r']=unique
x['p']=occurence 
x['pr']=x['p']/len(b3)

a_pr=x['pr'].to_numpy()
a_cdf=x['cdf'].to_numpy()
a_cdf=[sum(a_pr[0:m+1]) for m in range(len(unique))]
x['cdf']=a_cdf

x['s']=x['cdf']*255
    
    
a_s=x['s'].to_numpy()
arr_eq = np.zeros(250000)
    
for i in range(len(unique)):
    ix = np.where(b3 == unique[i])
    ix1 = ix[0]
    arr_eq[ix1] = a_s[i]

#recording for rgbHisto Equalisation
b_3=arr_eq   

arr_eq2d = arr_eq.reshape(500,500)

img=plt.imshow(arr_eq2d,cmap = 'gray')
plt.title('Histogram Equalization Band3')
plt.grid()
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(arr_eq2d),np.max(arr_eq2d)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('band3',dpi=150,quality=500)
plt.show()


#band4

path='C:/Users/harsh/Desktop/python/IDV/assignment3/orion/i170b4h0_t0.txt'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, header=None)

#flipping data
df=df.reindex(index=df.index[::-1])

#converting to array
band4=np.asarray(df)

b4=band4.reshape(500*500)
unique,occurence=np.unique(b4,return_counts=True)
    
list=['r','p','pr','cdf','s']
x=pd.DataFrame(index=unique,columns=list)
    
    
x['r']=unique
x['p']=occurence 
x['pr']=x['p']/len(b4)

a_pr=x['pr'].to_numpy()
a_cdf=x['cdf'].to_numpy()
a_cdf=[sum(a_pr[0:m+1]) for m in range(len(unique))]
x['cdf']=a_cdf

x['s']=x['cdf']*255
    
    
a_s=x['s'].to_numpy()
arr_eq = np.zeros(250000)
    
for i in range(len(unique)):
    ix = np.where(b4 == unique[i])
    ix1 = ix[0]
    arr_eq[ix1] = a_s[i]

#recording for rgbHisto Equalisation    
b_4=arr_eq    
arr_eq4 = arr_eq.reshape(500,500)

img=plt.imshow(arr_eq4,cmap = 'gray')
plt.title('Histogram Equalization Band4')
plt.grid()
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(arr_eq2d),np.max(arr_eq2d)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('band4',dpi=150,quality=500)
plt.show()


#RGB Histogram Equalization Image
rgb=[]
for i in range(500*500):
    rgb.append(b_4[i])
    rgb.append(b_3[i])
    rgb.append(b_1[i])
    
arr = np.array(rgb, dtype=np.int16) 
arr=arr.reshape(500,500,3)

img=plt.imshow(arr)
plt.title('Histo-Equalized RGB Image')
plt.grid()
cbar=plt.colorbar(img)
cbar.set_ticks([np.min(arr),np.max(arr)])
cbar.set_ticklabels(['low','high'])
cbar.set_label('density')
plt.savefig('rgbHisto',dpi=150,quality=500)
plt.show()