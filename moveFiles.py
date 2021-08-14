import os
import shutil
source = input("Source Folder Name: ")
destination = input("Enter Destination Folder Name: ")
source = source + '/'
destination = destination + '/'

listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.move((source+file),destination)