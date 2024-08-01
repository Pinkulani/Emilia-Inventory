import platform

def StartUp():
    OS = platform.system()
    if OS == "Darwin":
        OS = "macOS"
    
    print("OS:", OS)