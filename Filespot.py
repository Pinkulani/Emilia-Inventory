from tkinter import *
from tkinter import ttk

from Data.StartUp import StartUp
from Data.Folders import Folders
from Data.Files import Files

Start = StartUp()
Folders = Folders()
Files = Files()
XD = Files.GetExtension("Website.mp4")
XP = Files.GetType(XD)
print(XP)

Filespot = Tk()
Filespot.title("Filespot")

Style = ttk.Style()
Style.theme_use("clam")

Frame = ttk.Frame(Filespot)
Frame.grid()
#Frame.place(x = 0, y = 0)

ttk.Button(Frame, text="Start", command=lambda: Start.OSType()).grid(column = 1, row = 0)
ttk.Button(Frame, text="Create Folders", command=lambda: Folders.Create()).grid(column = 2, row = 0)
ttk.Button(Frame, text="List Files", command=lambda: Files.List()).grid(column = 1, row = 1)
ttk.Button(Frame, text="Quit", command=lambda: Filespot.destroy()).grid(column = 2, row = 1)

Filespot.mainloop()
