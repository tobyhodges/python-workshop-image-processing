# -*- coding: utf-8 -*-
"""
Created on Mon May 01 00:30:59 2017

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Quick & dirty script to generate illustrations for the python image
            analysis course's tutorial pipeline.
"""

# Imports
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


# GAUSSIAN KERNEL GRID

# Create the Gaussian kernel
a = np.zeros((11,11),dtype=np.uint8)
a[5,5] = 255
a = ndi.gaussian_filter(a,2)

# Generate figure
pig,ax = plt.subplots()
ax.matshow(a,cmap='Blues',vmax=12)

# Add the labels
for (i, j), z in np.ndenumerate(a*10):
    ax.text(j, i, z, ha='center', va='center')

# Cosmetics, saving and showing
plt.axis('off')
#plt.savefig('gaussian_kernel_grid.png')
plt.show()


# 1D ADAPTIVE THRESHOLDING

# Create 1D 'membrane' data
a = np.zeros(100) + 10
a[35] = 1000
a[65] = 1000
a = ndi.gaussian_filter(a,2)

# Create adaptive background
b = ndi.uniform_filter(a,size=20)

# Plot stuff
plt.plot(a)
plt.plot(b,c='r')
plt.ylim([-10,270])

# Label, save and show
plt.legend(['Raw 1D Membrane Signal','Adaptive Background'])
plt.xlabel('space [pixels]')
plt.ylabel('intensity [a.u.]')
#plt.savefig('adaptive_bg_1D.png')
plt.show()


# UNIFORM KERNEL WITH STRUCTURING ELEMENT

# Create data
i = 11
a = (np.mgrid[:i+2,:i+2][0] - np.floor(i/2) - 1)**2 + (np.mgrid[:i+2,:i+2][1] - np.floor(i/2) - 1)**2 <= np.floor(i/2)**2

# Generate figure
pig,ax = plt.subplots()
ax.matshow(a,cmap='Blues',vmax=2)

# Add the labels
for (i, j), z in np.ndenumerate(a*1):
    ax.text(j, i, z, ha='center', va='center')

# Cosmetics, saving and showing
plt.axis('off')
plt.savefig('uniform_filter_SE.png')
plt.show()
