# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:55:19 2022

@author: dell
"""

# This is a test script that reads and plots the TRMM 3B42 3-hourly data.
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC

import datetime as dt
from datetime import datetime

begin = dt.date(2014,7,2)  
length=287
date=[]
delta=dt.timedelta(days=1)
fr='D:/TRMM/3B42.{0}.{1}.7.HDF'
hour=['00','03','06','09','12','15','18','21']
theLats = np.arange(-49.875,50,0.25)
theLons = np.arange(-179.875,180,0.25)
fig = plt.figure(dpi=300)   #分辨率设为默认300比较合适
latcorners = ([-50,50])
loncorners = ([-180,180])

for i in range(length):
    date.append(begin.strftime("%Y%m%d"))
    begin += delta

for day in date:
    for hr in hour:
        fr1=fr.format(day,hr)
        dataset = SD(fr1, SDC.READ)
        precip = dataset.select('precipitation')
        precip = precip[:]
        precip = np.transpose(precip)
        # Set all the missing values less than 0 to NaNs
        np.putmask(precip,precip<0,np.nan)
        # Plot the figure, define the geographic bounds
        
        m = Basemap(projection='cyl',\
        llcrnrlat=latcorners[0],urcrnrlat=latcorners[1],llcrnrlon=loncorners[0],urcrnrlon=loncorners[1])
        # Draw coastlines, state and country boundaries, edge of map.
        m.drawcoastlines()
        m.drawstates()
        m.drawcountries()
        # Draw filled contours.
        clevs = np.arange(0,5.01,0.5)
        # Define the latitude and longitude data
        x, y = np.float32(np.meshgrid(theLons, theLats))
        cs = m.contourf(x,y,precip,clevs,cmap=cm.GMT_drywet,latlon=True)
        parallels = np.arange(-50.,51,25.)
        m.drawparallels(parallels,labels=[True,False,True,False])
        meridians = np.arange(-180.,180.,60.)
        m.drawmeridians(meridians,labels=[False,False,False,True])
        # Set the title and fonts
        titletext='{0} {1} UTC Rain Rate'.format(day, hr)
        plt.title(titletext)
        font = {'family' : 'normal', 'weight' : 'bold', 'size' : 6}
        plt.rc('font', **font)
        # Add colorbar
        cbar = m.colorbar(cs,location='right',pad="5%")
        cbar.set_label('mm/h')
        
        savepath='D:/TRMM/pictures/{0}_{1}.png'.format(day,hr)
        plt.savefig(savepath,dpi=300)
print("end")
