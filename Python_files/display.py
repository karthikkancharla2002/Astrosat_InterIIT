import pandas as pd
from tkinter import *
file1='D:\Club\Tech sec 2021\Inter IIT 2021 March\ASTROSAT\Astrosat_InterIIT\Python_files\Astrosat_readings_new.csv'
filedata=pd.read_csv(file1)

catalog_data = filedata[['Proposal_ID']]
print(catalog_data.head())


pid = input("Enter the required proposal ID: ")


dfpropid = filedata.loc[filedata['Proposal_ID'] == pid] 
dfpropid = dfpropid.set_index('Serial number')

print(dfpropid.head())

root = Tk()
 
# root window title and dimension
root.title("Welcome to ASTROSAT data analyzer")
# Set geometry (widthxheight)
root.geometry('500x100')

lbl = Label(root, text = "To see the various available catalogs ")
lbl.grid() 

# function to display text when
# button is clicked
def clicked():
    tableCatagData = []
    for catag in catalog_data:
        tableCatagData.append(catag)
    tableEle = []
    for catag in tableCatagData:
        tableEle.append(Label(root, text = catag))
    for tableLbl in range(len(tableEle)):
        tableEle[tableLbl].grid(column=0, row= tableLbl+2)    
    catView = []
    
# button widget with red color text
# inside
btn = Button(root, text = "Click here" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)


# all widgets will be here
# Execute Tkinter
root.mainloop()



