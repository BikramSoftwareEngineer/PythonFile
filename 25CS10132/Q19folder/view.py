import tkinter as tk
from tkinter import ttk

class LibraryView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library")
        self.ent = tk.Entry(self); self.ent.pack()
        
        f = tk.Frame(self); f.pack()
        self.b_add = tk.Button(f, text="Add"); self.b_add.pack(side="left")
        self.b_iss = tk.Button(f, text="Issue"); self.b_iss.pack(side="left")
        self.b_ret = tk.Button(f, text="Return"); self.b_ret.pack(side="left")
        self.b_src = tk.Button(f, text="Search"); self.b_src.pack(side="left")

        self.tree = ttk.Treeview(self, columns=("ID", "Title", "Status"), show="headings")
        for c in ("ID", "Title", "Status"): self.tree.heading(c, text=c)
        self.tree.pack()

    def show(self, rows):
        self.tree.delete(*self.tree.get_children())
        for r in rows: self.tree.insert("", "end", values=r)