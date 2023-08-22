import os

class Explorer(object):
    def __init__(self):
        print("Explorer")
        self.Directory = "../"
        self.FileList2 = os.listdir(self.Directory)
    
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
        self.FileList2 = os.listdir(self.Directory)

    def List(self):
        print("List of Files in Directory: ")
        self.UpdateFileList()
        for X in range(0, len(self.FileList2)):
            print(self.FileList2[X])

    def GetLastSection(self):
        Section = []
        #Checker = False # To check for the first /
        
        # Get Section till /
        for X in range(len(self.Directory)):
            if X == "/":
                #if Checker == False:
                #    Checker = True
                #else:
                break
            else:
                Section.append(X)
        
        print("Section: ", Section)
