import os
import shutil
source = input('Enter the source folder name: ')
destination = input('Enter Destination folder: ')
source = source+ '/'
destination= destination+'/'
listoffiles= os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file), destination)