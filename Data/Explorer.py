class Explorer(object):
    def __init__(self):
        print("Explorer")
        self.Directory = "../"
    def ChangeDirectory(self):
        Change = str(input("Change Directory: "))
        self.Directory = Change
    def GetDirectory(self):
        print("Current Directory: ", self.Directory)
