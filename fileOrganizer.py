import os
import shutil

#write the names of the directory here
path = input("Enter The Name Of The Directory To Be Sorted: ")
#list the file names
listOfFiles = os.listdir(path)

#creating for loop for going through each files
for file in listOfFiles:
    name,ext = os.path.splitext(file)
    ext = ext [1:]

    if ext == '':
        continue

    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)