import os
import shutil
import datetime

downloads = "C:/Users/romat/Downloads"
desktop = "C:/Users/romat/Desktop/"
dirlist = [downloads]
time = datetime.datetime.now().strftime("%Y%m%d")
os.chdir(downloads)

log_file = open(desktop + "filelog.txt", "a")

def write_log(file, action):
    if action == "delete":
        log_file.write(file + " is deleted at " + time + "\n")
    if action == "move":
        log_file.write(file + " is moved at " + time + "\n")
    
def delete_file(file):
    write_log(file = file, action = "delete")
    os.remove(file)
    
def move_file(file, folder):
    write_log(file = file, action = "move")
    shutil.move(file,  desktop + folder + "/" + file)

for directory in dirlist:
    for file in os.listdir(directory):
        ext2 = file[-2:]
        ext3 = file[-3:]
        ext4 = file[-4:]
        if ext3 == "exe" or ext3 == "msi" or ext3 == "zip" or ext3 == "mkv" or ext3 == "iso" or ext3 == "mp4" or ext2 == "js":
            delete_file(file)
        elif ext3 == "png" or ext3 == "jpg" or ext4 == "jfif":
            move_file(file, "pics")
        elif ext3 == "pdf":
            move_file(file, "pdfs")
        elif ext4 == "docx":
            move_file(file, "words")
        elif ext4 == "pptx":
            move_file(file, "presentations")
        elif file == "Telegram Desktop":
            shutil.rmtree(file)        

log_file.close()