import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
from astropy.io import ascii
tbl = ascii.read("Astrosat_readings_new.csv")
data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")
a=tbl['RA']
b= tbl['Dec']
#rounding of astrosat_RA(x)
x=[]
for i in range(len(a)):
    x.append(round(a[i],2));
#rounding off astrosat_dec(x2)
x2=[]
for i in range(len(b)):
    x2.append(round(b[i],2));
x2
#rounding of lmbx_RA(y)
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
#rounding of lmbx_Dec(y2)
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
source= data["NAME"]
        
for i in range(len(source)):
    if val==source[i]:
        r=y[i]
        r2=y2[i]
count=0
for i in range(len(x)):
    if r==x[i]:
        if x2[i]==r2:
            count=count+1
            print("detected by astrosat")
            print(tbl[i])
if count==0:
    print("Not detected by astrosat)
        
    
