import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("800x800") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.


# Wrapper 1 stores the introduction Message:
w1 = tk.LabelFrame(root)
# Wrapper 2 stores the remaining Content:
w2 = tk.LabelFrame(root)

w1.pack(fill="both",expand="yes",padx=10, pady=10)
w2.pack(fill="both",expand="yes",padx=10, pady=10)



# Frame for TreeView
frame1 = tk.LabelFrame(w2, text="List of Catalogs")
frame1.pack(fill="both",expand="yes",padx=10, pady=5) 

# Frame for open file dialog
file_frame = tk.LabelFrame(w2, text="Open File")
file_frame.pack(fill="both",expand="yes",padx=10, pady=5)

# Buttons
button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
button1.place(rely=0.7, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.7, relx=0.30)

# The file/file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)


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

def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information","No such file found")
        return None

    clear_data()
    catalog_data = df[['Proposal_ID']]
    catalog_ID_list = sorted(set(catalog_data['Proposal_ID'].array))    
    for i in range(len(catalog_ID_list)):
         tv1.insert('', 'end',values=(i+1,catalog_ID_list[i]))
    # tv1["column"] = list(df.columns)
    # tv1["show"] = "headings"
    # for column in tv1["columns"]:

    #     tv1.heading(column, text=column) # let the column heading = column name

    # df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    # for row in df_rows:
    #     tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()