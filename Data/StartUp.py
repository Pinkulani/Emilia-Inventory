import platform

class StartUp(object):
    def __init__(self):
        print("|- Filespot -|")
    def OSType(self):
        OS = platform.system()
        print("OS Type: ", end="")
        match OS:
            case "Darwin":
                print("macOS")
            case "Linux":
                print("Linux")
            case "Windows":
                print("Windows")
            case _:
                print("Unknown")
