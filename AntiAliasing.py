# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:06:07 2021

@author: 2rome
"""
import numpy as np
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors

@jit
def mandelbrot(z,maxiter,horizon,log_horizon):
    c = z
    for n in range(maxiter):
        az = abs(z)
        if az > horizon:
            print('Superado')
            print(az)
            print(z)
            print(n)
            return n - np.log(np.log(az))/np.log(2) + log_horizon
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    mandelbrot_values = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            mandelbrot_values[i,j] = mandelbrot(x_vals[i] + 1j*y_vals[j],maxiter,horizon, log_horizon)
    return x_vals,y_vals,mandelbrot_values

def save_image(fig):
    filename = "mandelbrot.png"
    fig.savefig(filename)

def mandelbrot_image(xmin=-2.0,xmax=0.5,ymin=-1.25,ymax=1.25,width=10,height=10,maxiter=80,cmap='jet',gamma=0.4):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    
    fig, ax = plt.subplots(figsize=(width, height),dpi=dpi)
    ticks = np.arange(0,img_width,3*dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    ax.set_title(cmap)
    
    norm = colors.PowerNorm(gamma)
    ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)  
    save_image(fig)

mandelbrot_image(maxiter=150, width = 10, height = 10)