import os
import shutil
import time

path = input("The path of the folder.")
days = input("Desired days old of the files you want to delete.")
ctime = str(os.stat(path).st_ctime)

os.path.exists(path)
os.walk(path)
os.path.join(path)
os.stat(path).st_ctime

if (ctime < days): 
    list_of_files = os.listdir(path)

    for file in list_of_files:
        name, ext = os.path.splitext(file)

        ext = ext[1:]

        if ext == '':
            continue

        if os.path.exists(path+'/'+ext):
            os.remove(path)

        else:
            shutil.rmtree(path)
