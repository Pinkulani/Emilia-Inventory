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
        #shutil.move("CheckParity.py", "../")

    def GetExtension(self, File):
        Extension = []

        # Get Extension
        for C in reversed(File):
            if C == ".":
                Extension.append(C)
                break
            else:
                Extension.append(C)

        # Reverse Extension into readable text
        Extension.reverse()

        # Built to String
        ExtensionString = ""
        for S in range(0, len(Extension)):
            ExtensionString += Extension[S]

        return ExtensionString
    
    def GetType(self, Extension):
        match Extension:
            case ".html":
                return "HTML"
            case ".py":
                return "Python"
            case ".cpp":
                return "C++"
            case ".gif":
                return "Gif"
            case ".png":
                return "Picture"
            case ".jpg":
                return "Picture"
            case ".mp4":
                return "Video"
            case _:
                return "Other"
