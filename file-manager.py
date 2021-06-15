#!/usr/bin/env python
# coding: utf-8


import os
import shutil

os.chdir("C:/Users/romat/Downloads")

for file in os.listdir("C:/Users/romat/Downloads"):
    if file[-3:] == "exe":
        os.remove(file)
    elif file[-3:] == "png" or file[-3:] == "jpg":
        shutil.move(file,  "C:/Users/romat/Desktop/pics/" + file)
    elif file[-3:] == "pdf":
        shutil.move(file,  "C:/Users/romat/Desktop/pdfs/" + file)