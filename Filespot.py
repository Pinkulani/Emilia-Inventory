from Data.StartUp import StartUp
from Data.Folders import Folders
from Data.Files import Files

Start = StartUp()
Start.OSType()

Folders = Folders()
Folders.Create()

Files = Files()
Files.List()
