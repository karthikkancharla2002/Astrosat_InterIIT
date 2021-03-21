import pandas as pd
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 


file1='D:\Club\Tech sec 2021\Inter IIT 2021 March\ASTROSAT\Astrosat_InterIIT\src\Astrosat_readings_new.csv'
filedata=pd.read_csv(file1)
## Storing unique catalog Proposal ids in a set
catalog_data = filedata[['Proposal_ID']]
catalog_list = set(catalog_data['Proposal_ID'].array)
## Applet code
root = Tk() 

# Wrapper 1 stores the introduction Message:
w1 = LabelFrame(root)
# Wrapper 2 stores the remaining Content:
w2 = LabelFrame(root)

w1.pack(fill="both",expand="yes",padx=10, pady=10)
w2.pack(fill="both",expand="yes",padx=10, pady=10)

# function to display text when
# button is clicked
def showSelectedCatalog(catalog):
    dfpropid = filedata.loc[filedata['Proposal_ID'] == catalog] 
    dfpropid = dfpropid.set_index('Serial number')
    print(dfpropid.head(10))
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 3), 
                 dpi = 100) 
    # list of squares 
    y = [i**2 for i in range(101)] 
  
    # adding the subplot 
    plot1 = fig.add_subplot(111) 
  
    # plotting the graph 
    plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = w1)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   w1) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()


def clicked():
    canvas_catalog_list = Canvas(w2)
    canvas_catalog_list.pack(side=LEFT, fill="both", expand="yes")

    yscrollbar = ttk.Scrollbar(w2,orient="vertical", command=canvas_catalog_list.yview )
    yscrollbar.pack(side=RIGHT, fill= "y")

    canvas_catalog_list.configure(yscrollcommand = yscrollbar.set)
    canvas_catalog_list.bind('<Configure>', lambda e: canvas_catalog_list.configure(scrollregion = canvas_catalog_list.bbox('all')))

    catalog_list_frame = Frame(canvas_catalog_list)
    # catalog_list_frame.pack()
    canvas_catalog_list.create_window((0,0),window = catalog_list_frame, anchor="nw")
    tableCatagData = []
    for catag in catalog_list:
        tableCatagData.append(catag)
    tableEle = []
    for catag in tableCatagData:
        tableEle.append(Button(catalog_list_frame, text = catag, command = lambda: showSelectedCatalog(catag)))
    for tableLbl in range(len(tableEle)):
        tableEle[tableLbl].pack()    
    catView = []



canvas_intro = Canvas(w1)
canvas_intro.pack(side=LEFT, fill="both", expand="yes")


lbl = Label(canvas_intro, text = "To see the various available catalogs ")
lbl.grid(row=0, column = 0) 
btn = Button(canvas_intro, text = "Click here" , fg = "red", command=clicked)
btn.grid(row = 0, column = 1)


# all widgets will be here
# Execute Tkinter
root.title("Welcome to ASTROSAT data analyzer")
root.geometry('500x500')

root.mainloop()



