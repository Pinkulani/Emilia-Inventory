import os
from Data.StartUp import *

Start = StartUp()
Start.OSType()

# Create Folders
Folders = ["../Pictures", "../Videos", "../Gifs"]
for X in range(0, len(Folders)):
    os.mkdir(Folders[X])
