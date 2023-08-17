import os
import pathlib
import shutil

class Files(object):
    def __init__(self):
        self.Path = "../"
    def List(self):
        print("List of Files in Directory: ")
        List = os.listdir(self.Path)
        for X in range(0, len(List)):
            print(List[X])
        
        # Test Move
        shutil.move("CheckParity.py", "../")
