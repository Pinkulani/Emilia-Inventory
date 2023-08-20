from tkinter import *
from tkinter import ttk

from Data.StartUp import StartUp
from Data.Folders import Folders
from Data.Files import Files
from Data.Explorer import Explorer

Start = StartUp()
Folders = Folders()
Files = Files()
Explorer = Explorer()

Filespot = Tk()
Filespot.title("Filespot")

Style = ttk.Style()
Style.theme_use("clam")

Frame = ttk.Frame(Filespot)
Frame.grid()

ttk.Button(Frame, text = "Sort", command=lambda: Files.Sort()).grid(column = 1, row = 0)
ttk.Button(Frame, text = "Create Folders", command=lambda: Folders.Create()).grid(column = 2, row = 0)
ttk.Button(Frame, text = "List Files", command=lambda: Files.List()).grid(column = 1, row = 1)
ttk.Button(Frame, text = "Quit", command=lambda: Filespot.destroy()).grid(column = 2, row = 1)

ttk.Button(Frame, text = "").grid(column = 1, row = 2)
ttk.Button(Frame, text = "").grid(column = 2, row = 2)

ttk.Button(Frame, text = "CD", command=lambda: Explorer.ChangeDirectory()).grid(column = 1, row = 3)
ttk.Button(Frame, text = "Get Directory", command=lambda: Explorer.GetDirectory()).grid(column = 2, row = 3)

Filespot.mainloop()
