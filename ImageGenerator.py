# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:58:05 2021

@author: 2rome
"""
from matplotlib import pyplot as plt
from matplotlib import colors

def save_image(fig):
    filename = "mandelbrot2.png"
    fig.savefig(filename)

def mandelbrot_image(xmin=-2.0,xmax=0.5,ymin=-1.25,ymax=1.25,width=10,height=10,maxiter=80,cmap='jet'):
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