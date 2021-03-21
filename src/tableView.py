from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def update(trv, n):
    for i in range(n):
        trv.insert('', 'end',values=('AID','AID2'))

root = Tk()
wrapper1 = LabelFrame(root, text="Catalog list")
wrapper2 = LabelFrame(root, text = "Search")
wrapper3 = LabelFrame(root, text= "Catalog data")

wrapper1.pack(fill="both", expand = "yes", padx = 20, pady = 30)
wrapper2.pack(fill="both", expand = "yes", padx = 20, pady = 10)
wrapper3.pack(fill="both", expand = "yes", padx = 20, pady = 10)

trv = ttk.Treeview(wrapper1, columns=(1,2), show="headings", height="6")
trv.pack(fill="x")

trv.heading(1, text = "CatalogID")
trv.heading(2, text = "CatalogID")
update(trv,50)

# trv.heading(3, text = "CatalogID")
# trv.heading(4, text = "CatalogID")




root.title("My application")
root.geometry("800x700")
root.mainloop()