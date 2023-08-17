import platform

class StartUp(object):
    def __init__(self):
        print("Filesort")
    def OSType(self):
        if platform.system() == "Darwin":
            print("macOS")
        else:
            print("Unknown")
