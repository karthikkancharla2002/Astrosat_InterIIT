import pandas as pd
tbl=pd.read_csv("Astrosat_readings_new.csv")
a=tbl["Source_name"]

val = input("Enter your value: ")

count=0;
for i in range(len(a)):
    if val==a[i]:
        print(tbl.loc[[i]]);
for i in range(len(a)):
    if val==a[i]:
        count=count+1;
        print("It was observed by Astrosat before");
        break;
if count==0:
    print(" It was not observed by Astrosat before")
