import numpy as np
# Set up matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
from astropy.io import *
data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")
data
data['RA']
import astropy.coordinates as coord
import astropy.units as u
new = []
for i in range(len(data)):
    i_row = data[i] # get the first (ith) row
    ra = coord.Angle(i_row["RA"], unit=u.hour) # create an Angle object
    print(ra.degree) # convert to degrees
    new.append(ra.degree)
new   
len(new)
ra = coord.Angle(new*u.degree)
ra = ra.wrap_at(180*u.degree)
import astropy.coordinates as coord
import astropy.units as u
new2 = []
for i in range(len(data)):
    i_row = data[i] # get the first (ith) row
    dec = coord.Angle(i_row["Dec"], unit=u.deg)
    print(dec.degree) # convert to degrees
    new2.append(dec.degree)
new2   
len(new2)
ra = coord.Angle(new*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(new2*u.degree)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
