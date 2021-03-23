import pandas as pd
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk, LabelFrame
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 
import numpy as np
import sys
import matplotlib.pyplot as plt
from astropy.io import ascii
import astropy.coordinates as astro_cords
import astropy.units as astro_units

currHoverData = []

def build_map():
    data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")
    
    ra_degree = []  #new
    dec_degree = [] #new2
    names = []

    for i in range(len(data)):
        i_row = data[i] # get the first (ith) row
        ra = astro_cords.Angle(i_row["RA"], unit=astro_units.hour) # create an Angle object
        ra_degree.append(ra.degree)
        dec = astro_cords.Angle(i_row["Dec"], unit=astro_units.deg)
        dec_degree.append(dec.degree)
        name = i_row["NAME"]
        names.append(name)

    ra = astro_cords.Angle(ra_degree*astro_units.degree)
    ra = ra.wrap_at(180*astro_units.degree)

    dec = astro_cords.Angle(dec_degree*astro_units.degree)

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection="mollweide")
    #scatter plot
    scat_plot = ax.scatter(ra.radian, dec.radian)
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)


    def update_annot(ind):
            pos = scat_plot.get_offsets()[ind["ind"][0]]
            annot.xy = pos
            text = ""
            if len(ind["ind"])>0:
                currHoverData = []
            for i in ind["ind"]:
                text+= " Source name : "+names[i]+"\n"
                currHoverData.append(names[i])
            annot.set_text(text)
            annot.get_bbox_patch()
            # .set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = scat_plot.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()
    fig.canvas.mpl_connect("motion_notify_event", hover)

    def onclick(event):
        cont, ind = scat_plot.contains(event)
        if cont:
            text = ""
            for i in ind["ind"]:
                text+= "Clicked Source name : "+names[i]+"\n"
                # currHoverData.append(names[i])
            print(text)
    fig.canvas.mpl_connect("button_press_event", onclick)
    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    ax.grid(True)
    plt.show()

## Applet code
root = Tk() 
# Wrapper 1 stores the Star Map:
w1 = LabelFrame(root)
w1.pack(fill="x",padx=10, pady=10)
# Wrapper 2 stores the Catalog content:
w2 = LabelFrame(root)
w2.pack(fill="both",expand="yes",padx=10, pady=10)

def makestarmap():
    build_map()
B = tk.Button(w1, text ="GetStarMap", command = makestarmap)
B.pack()

################ Wrapper 2 GUI #####################################

# Frame for TreeView
frame1 = tk.LabelFrame(w2, text="List of Catalogs")
frame1.pack(fill="both",expand="yes",padx=10, pady=5) 


astro_csv_file = './Astrosat_readings_new.csv'
df = pd.read_csv(astro_csv_file)

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