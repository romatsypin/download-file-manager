import os
import shutil
import datetime

downloads = "C:/Users/romat/Downloads"
desktop = "C:/Users/romat/Desktop/"
os.chdir(downloads)

log_file = open(desktop + "filelog.txt", "a")

def delete_file(file):
    log_file.write(file + " is deleted at " + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "\n")
    os.remove(file)
    
def move_file(file, folder):
    log_file.write(file + " is moved at " + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "\n")
    shutil.move(file,  desktop + folder + "/" + file)

for file in os.listdir(downloads):
    ext3 = file[-3:]
    if ext3 == "exe":
        delete_file(file)
    elif ext3 == "png" or file[-3:] == "jpg":
        move_file(file, "pics")
    elif ext3 == "pdf":
        move_file(file, "pdfs")

log_file.close()