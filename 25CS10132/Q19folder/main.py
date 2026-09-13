from model import LibraryModel
from view import LibraryView
from controller import LibraryController

m, v = LibraryModel(), LibraryView()
c = LibraryController(m, v)
v.mainloop()