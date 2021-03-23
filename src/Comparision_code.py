import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
def getData():    
    tbl = ascii.read("Astrosat_readings_new.csv")
    data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")
    a=tbl['RA']
    b= tbl['Dec']
    x=[]
    x2=[]
    for i in range(len(a)):
        x.append(round(a[i],2));
        x2.append(round(b[i],2));
    import astropy.coordinates as coord
    import astropy.units as u
    new = []
    y=[]
    for i in range(len(data)):
        i_row = data[i] # get the first (ith) row
        ra = coord.Angle(i_row["RA"], unit=u.hour) # create an Angle object
        print(ra.degree) # convert to degrees
        new.append(ra.degree)
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
        y2.append(round(new2[i],2))
    val = input("Enter your value: ")
    print(val)
    source= data["NAME"]
    r = 0
    r2 = 0
    for i in range(len(source)):
        if val==source[i]:
            r=y[i]
            r2=y2[i]
            print(source[i])
    exists = False
    data = []
    for i in range(len(x)):
        if r==x[i] and x2[i]==r2:
            data.append(tbl[i])
            exists = True
            # print(tbl[i])
    return data
data = getData()
print(len(data))     
