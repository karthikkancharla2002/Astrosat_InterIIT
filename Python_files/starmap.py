import numpy as np
import sys
!{sys.executable} -m pip install mpld3

# Set up matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
from astropy.io import ascii
data = ascii.read("lmxb_hmxb combined_cosmic sources.csv"
data['RA']
import astropy.coordinates as coord
import astropy.units as u
new = []
for i in range(len(data)):
    i_row = data[i] # get the first (ith) row
    ra = coord.Angle(i_row["RA"], unit=u.hour) # create an Angle object
    print(ra.degree) # convert to degrees
    new.append(ra.degree)  
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
ra = coord.Angle(new*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(new2*u.degree)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(projection="mollweide")
t=ax.scatter(ra.radian, dec.radian)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
labels = ['point {0}'.format(i + 1) for i in range(N)]
tooltip = mpld3.plugins.PointLabelTooltip(t, labels=labels)
mpld3.plugins.connect(fig, tooltip)
mpld3.show()


