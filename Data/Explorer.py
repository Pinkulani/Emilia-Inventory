import os

class Explorer(object):
    def __init__(self):
        print("Explorer")
        self.Directory = "../"
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
