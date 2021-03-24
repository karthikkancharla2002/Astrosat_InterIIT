import pandas as pd # imports and handles csv files
import tkinter as tk # creates templates for GUI files
from tkinter import Tk, filedialog, messagebox, ttk, LabelFrame # plotting library forms all plots like histogram, bar graph,etc.
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 
import numpy as np # mathematical tool helps in modifying the entire array at a time
import matplotlib.pyplot as plt
from astropy.io import ascii # main library helps in understanding and processing astronomical  data
import astropy.coordinates as astro_cords
import astropy.units as astro_units
import csv

publications_csv = "./publication.csv"
sources_csv_file = "lmxb_hmxb combined_cosmic sources.csv"
astro_csv_file = './Astrosat_readings_new.csv'

Title = 'Title'
Authors = 'Authors'
Bibliographi = 'Bibliographi'
Keywords = 'Keywords'
Abstract = 'Abstract'
URL = 'URL'

title_data = []
auth_data = []
bibl_data = []
keyword_data = []
abs_data = []
url_data = []

with open(publications_csv, 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row)>0:
            header = row[0].split()[0][:-1]
            if header == Title:
                title_data.append(row[0].split(':')[1].strip())
            elif header == Authors:
                auth_data.append(row[0].split(':')[1].strip())
            elif header == Bibliographi:
                bibl_data.append(row[0].split(':')[1].strip())
            elif header == Keywords:
                keyword_data.append(row[0].split(':')[1].strip())
            elif header == Abstract:
                abs_data.append(row[0].split(':')[1].strip())
            elif header == URL:
                url_data.append(row[0][5:].strip())

df_publications = pd.DataFrame([title_data, auth_data, bibl_data, keyword_data, abs_data, url_data], index=[Title,Authors,Bibliographi,Keywords,Abstract,URL]).T

def displayPublicationData(source_name, source_name2):
    df_selected_source_publication = df_publications[(df_publications.Title.str.replace(" ","").str.find(source_name.replace(" ","")) != -1) | (df_publications.Title.str.replace(" ","").str.find(source_name2.replace(" ","")) != -1) ]
    return df_selected_source_publication

def clickedSourceBox(n_data): 
    clickSourceRoot = Tk()  # creates a new window
    # Wrapper 1 stores the Star Map:
    wrapper_sources = LabelFrame(clickSourceRoot) # LabelFrame is hinged on its parent component which is clickSourceroot here and is stored in wrapper_sources
    wrapper_sources.pack(fill="both", expand="yes",padx=10, pady=10) # wrapper_sources is packed such that it fills both the axes, expands when required, padding with 10 pixels of padding in x and y directions 
    # Wrapper 2 stores the Catalog content:
    wrapper_data = LabelFrame(clickSourceRoot) # LabelFrame is hinged on its parent component which is clickSourceroot here and is stored in wrapper_data
    wrapper_data.pack(fill="both", expand="yes",padx=10, pady=10) # wrapper_data is packed such that it fills both the axes,expands when required, padding with 10 pixels of padding in x and y directions 
    frame1 = tk.LabelFrame(wrapper_sources, text="List of Clicked Sources") # frame 1 is hinged on wrapper_sources along with text 'List of Clicked Sources'
    frame1.pack(fill="both",expand="yes",padx=10, pady=5) # frame 1 is packed such that it fills both axes, is allowed to expand and paddying 10 pixels on x-axis and 5 pixels on y-axis
    file_frame = tk.LabelFrame(wrapper_data, text="Selected Source data") # file_frame is hinged on wrapper_data with text 'Selected Source data'
    file_frame.pack(fill="both",expand="yes",padx=10, pady=5) # file_frame is packed such that it fills both axes, is allowed to expand, and padding 10 pixels x-axis and 5 pixels on y-axis 
        
    publications_frame = tk.LabelFrame(wrapper_data, text="Publications")
    publications_frame.pack(fill="both",expand="yes",padx=10, pady=5)

    tv1s = ttk.Treeview(frame1, columns=["Sl.no", "Source_name"], show="headings", height="6") # Treeview shows the tables, is hinged to frame1, gives column ids, headings and height of each cell as 6
    tv1s.heading("Sl.no", text = "Sl.no") #column of ids and provided texts (identifiers)
    tv1s.heading("Source_name", text = "Source Name")  # columns are given names
    tv1s.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
    treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1s.yview) # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1s.xview) # command means update the xaxis view of the widget
    tv1s.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

    tv2 = ttk.Treeview(file_frame, show="headings", height="6") # Treeview shows the tables, is hinged to file_frame, gives column ids, headings and height of each cell as 6
    tv2.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
    treescrolly2 = tk.Scrollbar(file_frame, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
    treescrollx2 = tk.Scrollbar(file_frame, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget
    tv2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) # assign the scrollbars to the Treeview Widget
    treescrollx2.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly2.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget    
    
    tv3 = ttk.Treeview(publications_frame, show="headings", height="6")
    tv3.place(relheight=1, relwidth=1)
    treescrolly3 = tk.Scrollbar(publications_frame, orient="vertical", command=tv3.yview) # command means update the yaxis view of the widget
    treescrollx3 = tk.Scrollbar(publications_frame, orient="horizontal", command=tv3.xview) # command means update the xaxis view of the widget
    tv3.configure(xscrollcommand=treescrollx3.set, yscrollcommand=treescrolly3.set) # assign the scrollbars to the Treeview Widget
    treescrollx3.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly3.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
   
    for i in range(len(n_data)):
        tv1s.insert('', 'end',values=(i+1,n_data[i])) # inserts data in the tv in the end of the row with the values given
    
    def clear_window():
        tv2.delete(*tv2.get_children())
        tv3.delete(*tv2.get_children())
    
    def selectedSource(n_data):
        clear_window()
        s = tv1s.selection()[0]
        selected_source_name = tv1s.item(s,"values")[1]
        df_astrosat_data = getData(selected_source_name)
        astrosat_name = selected_source_name
        if (df_astrosat_data[df_astrosat_data.columns[0]].count())!=0:
            astrosat_name = df_astrosat_data['Source_name'].values[0]
        else:
            return
        tv2["column"] = list(df_astrosat_data.columns)
        tv2["show"] = "headings"
        for column in tv2["columns"]:
            tv2.heading(column, text=column) # let the column heading = column name
        df_rows2 = df_astrosat_data.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows2:
            tv2.insert("", "end", values=row) # inserts each list into the treeview. 
        
        df_publications_data = displayPublicationData(astrosat_name, selected_source_name)
        tv3["column"] = list(df_publications_data.columns)
        tv3["show"] = "headings"
        for column in tv3["columns"]:
            tv3.heading(column, text=column) # let the column heading = column name
        df_rows2 = df_publications_data.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows2:
            tv3.insert("", "end", values=row) # inserts each list into the treeview. 
    tv1s.bind("<Double-1>", lambda n_data:  selectedSource(n_data)) # lambda funtion seta parameters that need to be passed, define events with custom parameters
    clickSourceRoot.title("Welcome to ASTROSAT data analyzer")
    clickSourceRoot.geometry('800x800')
    clickSourceRoot.mainloop()

def getData(source_name):  
    df_sources = pd.read_csv(sources_csv_file) # df_sources stores the data from the sources_csv_files
    df_astrosat = pd.read_csv(astro_csv_file) # dfastrosat stores the data from the astro_csv_file
    row_source = df_sources[df_sources['NAME'] == source_name] # query asks the name of the datasource from the source_name
    r = round(astro_cords.Angle(row_source["RA"].values[0], unit=astro_units.hour).degree,2) # ra(row sources) values stored in an array and then rounded off to 2 decimal places
    r2 = round(astro_cords.Angle(row_source["Dec"].values[0], unit=astro_units.deg).degree,2) # declination values stored in an array and then rounded off to 2 decimal places
    result = df_astrosat[round(df_astrosat['RA'],2) == r] # query checking the rounded off 'ra' data upto 2 decimal places from astrosat and source file
    result = result[round(result['Dec'],2) == r2] # query checking the rounded off 'dec' data upto 2 decimal places from astrosat and source file
    return result # result is returned

def build_map():
    data = ascii.read("lmxb_hmxb combined_cosmic sources.csv") # ascii reads the source file
    ra_degree = []  #new  #angle co-ordinate of the point
    dec_degree = [] #new2 #declination co-ordinate of the point
    names = [] # name of the point
    for i in range(len(data)):
        i_row = data[i] # get the first (ith) row
        ra = astro_cords.Angle(i_row["RA"], unit=astro_units.hour) # create an Angle object
        ra_degree.append(ra.degree) # store it in re_degree list
        dec = astro_cords.Angle(i_row["Dec"], unit=astro_units.deg) # creates an Declination object
        dec_degree.append(dec.degree) # store it in dec_degree list
        name = i_row["NAME"] #creates a name object
        names.append(name) # stores it in names list
    ra = astro_cords.Angle(ra_degree*astro_units.degree)
    ra = ra.wrap_at(180*astro_units.degree)
    dec = astro_cords.Angle(dec_degree*astro_units.degree)
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection="mollweide") # mollweide provides globe like view
    #scatter plot
    scat_plot = ax.scatter(ra.radian, dec.radian)
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    def update_annot(ind):
            pos = scat_plot.get_offsets()[ind["ind"][0]]
            annot.xy = pos
            text = ""
            if len(ind["ind"])>0: # if point exists
                currHoverData = [] # currenthover data defined  
            for i in ind["ind"]: 
                text+= " Source name : "+names[i]+"\n" # taking name instead of whole address
                df_astrosat_data = getData(names[i]) # checks if the name is present in astrosat data function or not and returning to 'd'
                if (df_astrosat_data[df_astrosat_data.columns[0]].count())==0: #if length of d is 0 i.e. it does not exists
                    text+= " Astrosat : False"+"\n" # it prints 'False'
                else:
                    text+= " Astrosat : True"+"\n" # otherwise it prints true
                currHoverData.append(names[i])
            annot.set_text(text) #setting text
            annot.get_bbox_patch() # getting back, setting things like colour
            # .set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

    def hover(event): 
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = scat_plot.contains(event)
            if cont:  # check if pointer coincide with given event , if yes
                update_annot(ind)
                annot.set_visible(True)  # shows the data
                fig.canvas.draw_idle() # otherwise left idle
            else:
                if vis:
                    annot.set_visible(False) # if pointer is stationary
                    fig.canvas.draw_idle() # data should be shown stationary
    fig.canvas.mpl_connect("motion_notify_event", hover) # canvas inside figure is selected with the help of mpl connect, and then hover function works whenever the mouse hovers over the figure


    def onclick(event):
        cont, ind = scat_plot.contains(event) # checks is pointer clicks on datapoint or not
        if cont: # it it does
            text = ""
            obtainedData = [] # we obtain data array
            for i in ind["ind"]:
                obtainedData.append(names[i]) # append all the names in the index
            clickedSourceBox(obtainedData) # opens another window
    fig.canvas.mpl_connect("button_press_event", onclick) # if datapoint is clicked, function is triggered
    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    ax.grid(True)
    plt.show()

## Applet code
root = Tk() # Tk provies us widgets and returns windows and windows is then stored in 'root'
# Wrapper 1 stores the Star Map:
w1 = LabelFrame(root) # LabelFrame is hinged on its parent component which is root here and is stored in w1
w1.pack(fill="x",padx=10, pady=10) # w1 is packed such that it fills the entire x-axis along with 10 pixels of padding in x and y directions 
# Wrapper 2 stores the Catalog content:
w2 = LabelFrame(root) 
w2.pack(fill="both",expand="yes",padx=10, pady=10) # w2 fills both x & y axes, is allowed to expand as required and padding of 10 pixels in both axes

def makestarmap():
    build_map() 


heading = tk.Label( w1, text="VISUALIZATION TOOL FOR ASTROSAT OBSERVATIONS", font=("Arial", 15))
heading.pack()

file_input_frame_alpha = tk.LabelFrame(w1, text="Import Files")
file_input_frame_alpha.pack(fill="x",expand="yes",padx=10, pady=10)

# astrosat data file
file_frame_astrosat_data = tk.LabelFrame(file_input_frame_alpha, text="Astrosat Data File")
file_frame_astrosat_data.pack(side="left",expand="yes",padx=10, pady=10,fill = tk.BOTH)
label_file_text = "No File Selected"
varast = tk.StringVar()
label_file = ttk.Label(file_frame_astrosat_data, textvariable=varast)
varast.set(label_file_text[-25:])
label_file.pack(fill="x",expand="yes",padx=10, pady=2)
button1_astrosat_data = tk.Button(file_frame_astrosat_data, text="Browse A File", command=lambda: File_dialog(label_file_text, varast))
button1_astrosat_data.pack(fill="x",expand="yes",padx=10, pady=2)
button2_astrosat_data = tk.Button(file_frame_astrosat_data, text="Load File", command=lambda: Load_excel_data(astro_csv_file, label_file_text))
button2_astrosat_data.pack(fill="x",expand="yes",padx=10, pady=2)

# Sources Data
file_frame_sources_data = tk.LabelFrame(file_input_frame_alpha, text="Sources Data File")
file_frame_sources_data.pack(side="left",expand="yes",padx=10, pady=10, fill = tk.BOTH)
label_file_sources_text = "No File Selected"
varsou = tk.StringVar()
label_file_sources = ttk.Label(file_frame_sources_data, textvariable=varsou)
varsou.set( label_file_sources_text[-25:])
label_file_sources.pack(fill="x",expand="yes",padx=10, pady=2)
button1_sources_data = tk.Button(file_frame_sources_data, text="Browse A File", command=lambda: File_dialog(label_file_sources_text, varsou))
button1_sources_data.pack(fill="x",expand="yes",padx=10, pady=2)
button2_sources_data = tk.Button(file_frame_sources_data, text="Load File", command=lambda: Load_excel_data(sources_csv_file, label_file_sources_text))
button2_sources_data.pack(fill="x",expand="yes",padx=10, pady=2)

# Publications Data
file_frame_publications_data = tk.LabelFrame(file_input_frame_alpha, text="Publications Data File")
file_frame_publications_data.pack(side="left",expand="yes",padx=10, pady=10, fill = tk.BOTH)
label_file_publications_text = "No File Selected"
varpub = tk.StringVar()
label_file_publications = ttk.Label(file_frame_publications_data, textvariable=varpub)
varpub.set(label_file_publications_text[-25:])
label_file_publications.pack(fill="x",expand="yes",padx=10, pady=2)
button1_publications_data = tk.Button(file_frame_publications_data, text="Browse A File", command=lambda: File_dialog(label_file_publications_text, varpub))
button1_publications_data.pack(fill="x",expand="yes",padx=10, pady=2)
button2_publications_data = tk.Button(file_frame_publications_data, text="Load File", command=lambda: Load_excel_data(publications_csv, label_file_publications_text))
button2_publications_data.pack(fill="x",expand="yes",padx=10, pady=2)


def File_dialog(label_file, var):
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file = filename
    var.set(label_file[-25:])
    return None

def Load_excel_data(pathToSet, label_file):
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file
    try:
        excel_filename = "{}".format(file_path)
        print(excel_filename)
        if excel_filename[-4:] == ".csv":
            pathToSet = excel_filename
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", "No such file as {}".format(file_path))
        return None


B = tk.Button(w1, text ="Generate Map", command = makestarmap , bg="white")
B.pack(fill="both",expand="yes",padx=10, pady=10)

################ Wrapper 2 GUI #####################################

# Frame for TreeView
frame1 = tk.LabelFrame(w2, text="List of Catalogs") # frame 1 is hinged on w2 along with text 'List of Catalogs'
frame1.pack(fill="both",expand="yes",padx=10, pady=5) # frame 1 is packed such that it fills both axes, is allowed to expand and paddying 10 pixels on both axes


df = pd.read_csv(astro_csv_file) # pandas read the csv file which is returned in dataframe

# Frame for Selected Catalog 
file_frame = tk.LabelFrame(w2, text="Selected Catalog") # file_frame is hinged on w2 with text 'Selected Catalog'
file_frame.pack(fill="both",expand="yes",padx=10, pady=5) # file_frame is packed such that it fills both axes, is allowed to expand, and padding 10 pixels to both axes 


## Treeview Widget
tv1 = ttk.Treeview(frame1, columns=["Sl.no", "Catalog_ID"], show="headings", height="6") # Treeview shows the tables, is hinged to frame1, gives column ids, headings and height of each cell
tv1.heading("Sl.no", text = "Sl.no") #column of ids and provided texts (identifiers)
tv1.heading("Catalog_ID", text = "Catalog ID") # columns are given names
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget

treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



catalog_data = df[['Proposal_ID']] # lookin in df for the column having name 'Proposal_ID'
catalog_ID_list = sorted(set(catalog_data['Proposal_ID'].array)) # converts the entire dataframe's column in array and stores it in a set. It removes duplicate things. sorted converts it into a alphabetically sorted list. the entire sorted list is stored in catalog ID list
for i in range(len(catalog_ID_list)): # 
    tv1.insert('', 'end',values=(i+1,catalog_ID_list[i])) #  insert adds a new row in the end of treeview with parent component heading filled with given values (i+1 with catalog list id)

def OnDoubleClick(event): # on doubleclick, the builtin event will take place
        clear_data() # clears all the existing data 
        s = tv1.selection()[0] 
        selected_catalog_id = tv1.item(s,"values")[1] # gets the name catalog
        df2 = df.loc[df['Proposal_ID'] == str(selected_catalog_id)] # query checks if proposal id equals catalog id, its being added up
        tv2["column"] = list(df2.columns) # treewview should have same columns as df2 columns
        tv2["show"] = "headings" # shows all its headings
        for column in tv2["columns"]:
            tv2.heading(column, text=column) # let the column heading = column name
        df_rows2 = df2.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows2:
            tv2.insert("", "end", values=row) # inserts each list into the treeview. 
tv1.bind("<Double-1>", OnDoubleClick) # doubleclick binds 

## Treeview Widget
tv2 = ttk.Treeview(file_frame, show="headings", height="6") # Treeview shows the table, hinged to file_framer, shows headings and sets height of cells as 6
tv2.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (file_frame).

treescrolly2 = tk.Scrollbar(file_frame, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
treescrollx2 = tk.Scrollbar(file_frame, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget

tv2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) # assign the scrollbars to the Treeview Widget

treescrollx2.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly2.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

def clear_data():  #clears the data from the table
    tv2.delete(*tv2.get_children()) 
    return None

# Execute Tkinter
root.title("Welcome to ASTROSAT data analyzer") # sets the title
root.geometry('800x800') # sets the geometry in pixels
root.mainloop() # only executable function in Tkinter class, makes all the codes visible on running 