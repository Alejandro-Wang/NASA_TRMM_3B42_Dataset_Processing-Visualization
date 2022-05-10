# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:43:48 2022

@author: dell
"""
import imageio
from pathlib import Path

date=['02','03','04','05','06','07','08','09','10','11','12']
hour=['00','03','06','09','12','15','18','21']
path='D:/TRMM/pictures/201407{0}_{1}.png'

def create_gif(image_list, saveName, duration,loop):
    '''
    

    Parameters
    ----------
    img_list : list
    saveName : TYPE
    duration : 图像间隔时间 interval time. The default is 0.1.
    loop : gif loop type. The default is 0.
    '''
    frames=[]
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(saveName, frames, 'GIF', duration=duration,loop=0)
    return
def merge_gif():
    image_list=[]
    duration=0.1
    loop=0
    for day in date:
        for hr in hour:
            image_list.append(path.format(day, hr))
            saveName='D:/TRMM/pictures/Global Rain Rate Dynamic Evolution.gif'
            return
    create_gif(image_list, saveName,duration,loop)

if __name__ == '__main__':
    merge_gif()    