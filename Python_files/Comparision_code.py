import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
from astropy.io import ascii
tbl = ascii.read("Astrosat_readings_new.csv")
data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")

import astropy.coordinates as coord
import astropy.units as u
new = []
for i in range(len(data)):
    i_row = data[i] # get the first (ith) row
    ra = coord.Angle(i_row["RA"], unit=u.hour) # create an Angle object
    print(ra.degree) # convert to degrees
    new.append(ra.degree)
y=[]
for i in range(len(new)):
    y.append(round(new[i],2));

import astropy.coordinates as coord
import astropy.units as u
new2 = []
for i in range(len(data)):
    i_row = data[i] # get the first (ith) row
    dec = coord.Angle(i_row["Dec"], unit=u.deg)
    print(dec.degree) # convert to degrees
    new2.append(dec.degree)
y2=[]
for i in range(len(new2)):
    y2.append(round(new2[i],2));
val = input("Enter your value: ")
source= tbl["Source_name"]
w= tbl['RA']
q= tbl['Dec']
for i in range(len(tbl)):
    if source[i]==val:
        index=i;
for i in range(len(source)):
    if val==source[i]:
        r=round(w[i],2)
        r2=round(q[i],2)
for i in range(len(y)):
    if r==y[i]:
        if y2[i]==r2:
            print("detected by astrosat")
            print(tbl[index])
        else:
            print("not detected by astrosat")
