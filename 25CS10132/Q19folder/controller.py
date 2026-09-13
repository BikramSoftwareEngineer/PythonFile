class LibraryController:
    def __init__(self, m, v):
        self.m, self.v = m, v
        v.b_add.config(command=lambda: (m.add(v.ent.get(), "Book"), self.load()))
        v.b_iss.config(command=lambda: (m.status(v.ent.get(), "Issued"), self.load()))
        v.b_ret.config(command=lambda: (m.status(v.ent.get(), "Available"), self.load()))
        v.b_src.config(command=lambda: v.show(m.search(v.ent.get())))
        self.load()

    def load(self):
        self.v.show(self.m.search(""))