# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:05:43 2021

@author: Samuel OH
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io, morphology



#CRECIMIENTO DE REGIÓN 
#MORFOLOGÍA SE REFIERE A LA DILATACIÓN, EROCIÓN DE UNA IMAGEN


#####################CARGAR__LAS__IMAGENES###############
'''imagen = io.imread('29.jpg')
gris = color.rgb2gray(imagen)*255





#########################MOSTRAR___IMAGENES#################
plt.figure(1)
plt.title('IMAGEN ORIGINAL')
plt.axis('off')
plt.imshow(imagen)



plt.figure(2)
plt.title('IMAGEN ESCALA DE GRISES')
plt.axis('off')
plt.imshow(gris, cmap = 'gray')


plt.ion() #LA FUNCIÓN ION REFIERE A INTERACTIVE ON


#####################INICIO__DEL__METODO################

tolerancia = 15 #ESTE VALOR NO DICE QUE SI EL PIXEL VECINO CON UNA VALOR +- 15, EL PIXEL SE PARECE AL PIXEL DEL CENTRO
posicion = np.int32(plt.ginput(0,0)) #SE SOLICITARIA AL USUARIO DONDE COLOCAR LA SEMILLA DE LA IMAGEN
filas , columnas = gris.shape

phi = np.zeros((filas,columnas ),dtype = np.byte) #ESTA VARIABLE NOS SIRVE COMO UNA GUÍA PARA DETENER LA EXPANCIÓN, DE MODO QUE EL PHI NUEVO Y EL PHI OLD SEAN IGUALES ESTA DEBERA PARAR
phiOld = np.zeros ((filas,columnas ), dtype = np.byte)




phi[posicion[:,1], posicion[:,0]] = 1
pixeles = gris[posicion[:,1], posicion[:,0]]
promedio = np.mean(pixeles)


while( np.sum(phiOld) != np.sum(phi) ):
    plt.cla()
    phiOld = np.copy(phi)
    bordes = morphology.binary_dilation(phi) - phi #SOLO SE QUEDAN LOS PIXELES QUE FUERON AUMENTADOS
    newPos = np.argwhere(bordes)#EL ARGUMENTO DE LOS BORDES
    newPix = gris[newPos[:,0], newPos[:,1]] #SE GUARDAN LOS VALORES DE LOS PIXELES EXPANDIDOS
    compara = list(np.logical_and([newPix > promedio - tolerancia], [newPix < promedio + tolerancia])) #SE REALIZA UNA COMPARACIÓN CON LOS VALORES EXPANDIDOS CON EL USO DEL PRIMEDIO Y LA TOLERANCIA 
    datos = newPos[compara] #AHORA SE GUARDAN LOS VALORES QUE CUMPLIERON LA COMPARATIVA 
    phi[ datos[:,0], datos[:,1] ] = 1 #AQUI EN PHI SE COLOCA UN 1 EN LAS POSICIONES QUE FUERON GUARDADAS 
    plt.imshow(phi, cmap = 'gray')
    plt.pause(0.01)



plt.figure(2)
plt.axis('off')
plt.imshow(gris, cmap = 'gray')
plt.show()

plt.figure(3)
plt.axis('off')
plt.imshow(phi, cmap = 'gray')
plt.show()


im3D = np.zeros((filas,columnas,10))
im3D[:,:,0] = phi


plt.figure(4)
plt.imshow(im3D[:,:,0],cmap = 'gray' )
plt.imshow()'''

def crecimiento (gris):
    
    plt.figure(2)
    plt.title('IMAGEN ESCALA DE GRISES')
    plt.axis('off')
    plt.imshow(gris, cmap = 'gray')
    plt.ion() #LA FUNCIÓN ION REFIERE A INTERACTIVE ON
    
    tolerancia = 15 #ESTE VALOR NO DICE QUE SI EL PIXEL VECINO CON UNA VALOR +- 15, EL PIXEL SE PARECE AL PIXEL DEL CENTRO
    posicion = np.int32(plt.ginput(0,0)) #SE SOLICITARIA AL USUARIO DONDE COLOCAR LA SEMILLA DE LA IMAGEN
    filas , columnas = gris.shape
    
    phi = np.zeros((filas,columnas ),dtype = np.byte) #ESTA VARIABLE NOS SIRVE COMO UNA GUÍA PARA DETENER LA EXPANCIÓN, DE MODO QUE EL PHI NUEVO Y EL PHI OLD SEAN IGUALES ESTA DEBERA PARAR
    phiOld = np.zeros ((filas,columnas ), dtype = np.byte)
    
    phi[posicion[:,1], posicion[:,0]] = 1
    pixeles = gris[posicion[:,1], posicion[:,0]]
    promedio = np.mean(pixeles)
    
    
    while( np.sum(phiOld) != np.sum(phi) ):
        plt.cla()
        phiOld = np.copy(phi)
        bordes = morphology.binary_dilation(phi) - phi #SOLO SE QUEDAN LOS PIXELES QUE FUERON AUMENTADOS
        newPos = np.argwhere(bordes)#EL ARGUMENTO DE LOS BORDES
        newPix = gris[newPos[:,0], newPos[:,1]] #SE GUARDAN LOS VALORES DE LOS PIXELES EXPANDIDOS
        compara = list(np.logical_and([newPix > promedio - tolerancia], [newPix < promedio + tolerancia])) #SE REALIZA UNA COMPARACIÓN CON LOS VALORES EXPANDIDOS CON EL USO DEL PRIMEDIO Y LA TOLERANCIA 
        datos = newPos[compara] #AHORA SE GUARDAN LOS VALORES QUE CUMPLIERON LA COMPARATIVA 
        phi[ datos[:,0], datos[:,1] ] = 1 #AQUI EN PHI SE COLOCA UN 1 EN LAS POSICIONES QUE FUERON GUARDADAS 
        plt.imshow(phi, cmap = 'gray')
        plt.pause(0.01)


    return phi
'''
imagen = io.imread('27.jpg')
gris =  color.rgb2gray(imagen)*255

imagen_procesada = crecimiento(gris)'''
