# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:51:41 2021

@author: PC
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology, feature,io,color
from crecimiento_de_regiones import crecimiento 


plt.close('all')


im = cv2.imread('Brain.png')
gris_o = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im2 = im.reshape((-1,3))
im2 = np.float32(im2)
criterio = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1 )
k = 4
intentos = 10
ret, label, center = cv2.kmeans(im2, k, None, criterio, intentos, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
rescale = center[label.flatten()]
rescaleF = rescale.reshape((im.shape))
gray = cv2.cvtColor(rescaleF, cv2.COLOR_BGR2GRAY)
plt.figure(1)
plt.imshow(gray, cmap = 'gray')
plt.axis('off')





estructure = morphology.disk(4.5)
open_image = morphology.opening(gray,estructure)



segmento = crecimiento(open_image)


imagen_f = segmento * gris_o


plt.figure('f')
plt.axis('off')
plt.imshow(imagen_f , cmap = 'gray')




'''
plt.figure(2)
plt.imshow(open_image, cmap = 'gray')
plt.axis('off')
binario = (open_image > 183)
binario2 = binario * gris_o
edge = feature.canny(binario2,sigma = 2)
plt.figure(3)
plt.imshow(binario2, cmap = 'gray')
plt.axis('off')
salida = (edge * 255) + gris_o
plt.figure(4)
plt.imshow(salida, cmap = 'gray')
plt.axis('off')
'''
    



