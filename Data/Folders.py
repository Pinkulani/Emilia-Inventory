import os

class Folders(object):
    def __init__(self):
        pass
    def Create(self):
        Folders = ["../Pictures", "../Videos", "../Gifs", "../HTML", "../Python"]
        for X in range(0, len(Folders)):
            if os.path.exists(Folders[X]):
                print("Folder already exists")
            else:
                print("Folder created")
                os.mkdir(Folders[X])
