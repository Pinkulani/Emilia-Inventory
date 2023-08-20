import os

class Explorer(object):
    def __init__(self):
        print("Explorer")
        self.Directory = "../"
        self.FileList = os.listdir(self.Directory)
    
    def ChangeDirectory(self):
        print("CD needs to come from Filespot.py directory")
        Change = str(input("Change Directory: "))
        Check = self.Directory + Change
        if os.path.isdir(Check) == True:
            print("Directory changed")
            self.Directory = Check
        else:
            print("Directory not found")
    
    def GetDirectory(self):
        print("Current Directory: ", self.Directory)
    
    def UpdateFileList(self):
        self.FileList = os.listdir(self.Directory)

    def List(self):
        print("List of Files in Directory: ")
        self.UpdateFileList()
        for X in range(0, len(self.FileList)):
            print(self.FileList[X])
