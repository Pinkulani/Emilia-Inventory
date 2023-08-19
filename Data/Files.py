import os
import pathlib
import shutil

class Files(object):
    def __init__(self):
        self.Path = "../"
        self.FileList = os.listdir(self.Path)

    def List(self):
        print("List of Files in Directory: ")
        for X in range(0, len(self.FileList)):
            print(self.FileList[X])

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

    def Sort(self):
        for L in range(0, len(self.FileList)):
            CurrentFile = self.GetExtension(self.FileList[L])
            CurrentFile = self.GetType(CurrentFile)
            
            # Reverse Filename
            Filepath = self.FileList[L][::-1]

            # Add ../ to fetch files from Top Folder
            Filepath += "/.."
            
            # Reverse Filename again to get correct Filepath
            Filepath = Filepath[::-1]
            
            # Current File = File Type
            match CurrentFile:
                case "Picture":
                    shutil.move(Filepath, "../Pictures")
                case "Video":
                    shutil.move(Filepath, "../Videos")
                case "Python":
                    shutil.move(Filepath, "../Python")
                case _: # Don't move Folders
                    continue
