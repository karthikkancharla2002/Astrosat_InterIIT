import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 
from tkinter import *

# file1='D:\Club\Tech sec 2021\Inter IIT 2021 March\ASTROSAT\Astrosat_InterIIT\src\Astrosat_readings_new.csv'
# filedata=pd.read_csv(file1)
# ## Storing unique catalog Proposal ids in a set
# catalog_data = filedata[['Proposal_ID']]
# catalog_list = set(catalog_data['Proposal_ID'].array)

## Applet code
root = Tk() 
# Wrapper 1 stores the Star Map:
w1 = LabelFrame(root)
w1.pack(fill="x",padx=10, pady=10)
# Wrapper 2 stores the Catalog content:
w2 = LabelFrame(root)
w2.pack(fill="both",expand="yes",padx=10, pady=10)

# all widgets will be here
################ Wrapper 1 GUI #####################################
# PLOTTING THE FIGURE
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
x = np.random.rand(15)
y = np.random.rand(15)
names = np.array(list("ABCDEFGHIJKLMNO"))
c = np.random.randint(1,5,size=15)

norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn

fig,ax = plt.subplots()
canvas_starplot2 = FigureCanvasTkAgg(fig, master = w1)   
canvas_starplot2.draw() 
sc = fig.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)
sc = ax.scatter(ra.radian, dec.radian)
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)
# ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
# ax.grid(True)
# plt.show()
# placing the canvas on the Tkinter window 
canvas_starplot2.get_tk_widget().pack() 
# creating the Matplotlib toolbar 
toolbar = NavigationToolbar2Tk(canvas_starplot2, w1) 
toolbar.update() 
# placing the toolbar on the Tkinter window 
canvas_starplot2.get_tk_widget().pack()

################ Wrapper 2 GUI #####################################

# Frame for TreeView
frame1 = tk.LabelFrame(w2, text="List of Catalogs")
frame1.pack(fill="both",expand="yes",padx=10, pady=5) 

# Frame for Selected Catalog 
file_frame = tk.LabelFrame(w2, text="Selected Catalog")
file_frame.pack(fill="both",expand="yes",padx=10, pady=5)
df = pd.read_csv('Astrosat_readings_new.csv')

## Treeview Widget
tv1 = ttk.Treeview(frame1, columns=["Sl.no", "Catalog_ID"], show="headings", height="6")
tv1.heading("Sl.no", text = "Sl.no")
tv1.heading("Catalog_ID", text = "Catalog ID")
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

catalog_data = df[['Proposal_ID']]
catalog_ID_list = sorted(set(catalog_data['Proposal_ID'].array))    

def OnDoubleClick(event):
        clear_data()
        s = tv1.selection()[0]
        selected_catalog_id = tv1.item(s,"values")[1]
        df2 = df.loc[df['Proposal_ID'] == str(selected_catalog_id)]
        tv2["column"] = list(df2.columns)
        tv2["show"] = "headings"
        for column in tv2["columns"]:
            tv2.heading(column, text=column) # let the column heading = column name
        df_rows2 = df2.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows2:
            tv2.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert

for i in range(len(catalog_ID_list)):
    tv1.insert('', 'end',values=(i+1,catalog_ID_list[i]))
tv1.bind("<Double-1>", OnDoubleClick)

## Treeview Widget
tv2 = ttk.Treeview(file_frame, show="headings", height="6")
tv2.place(relheight=1, relwidth=1)
treescrolly2 = tk.Scrollbar(file_frame, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
treescrollx2 = tk.Scrollbar(file_frame, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget
tv2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) # assign the scrollbars to the Treeview Widget
treescrollx2.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly2.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

def clear_data():
    tv2.delete(*tv2.get_children())
    return None
# Execute Tkinter
root.title("Welcome to ASTROSAT data analyzer")
root.geometry('800x800')
root.mainloop()



