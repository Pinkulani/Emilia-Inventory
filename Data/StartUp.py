import platform

class StartUp(object):
    def __init__(self):
        print("Filesort")
    def OSType(self):
        OS = platform.system()
        print("OS: ", end="")
        match OS:
            case "Darwin":
                print("macOS")
            case "Linux":
                print("Linux")
            case "Windows":
                print("Windows")
            case _:
                print("Unknown")
