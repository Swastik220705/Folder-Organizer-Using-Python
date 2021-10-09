# ---------------------- Automatic Folder Organizer ---------------------- #

"""
Made By Swastik
Date - 09/10/2021
"""
import os
directory = input("Enter path of folder you want to organize: ")
os.chdir(directory)
folders = ["Audio", "Video", "Images", "Documents", "Applications", "Folders", "Archives",  "Others"]
for folder in folders:
    if not os.path.isdir(folder):
        os.makedirs(folder)

extentions = {"Audio": [".wav", ".aac", ".mp3"],
              "Video": [".mp4", ".mkv", ".wmv", ".webm"],
              "Images": [".jpg", ".jpeg", ".png"],
              "Documents": [".pdf", ".docx", ".pptx", ".html", ".py", ".mhtml", ".txt"],
              "Applications": [".exe", ".msi"],
              "Folders": [folder for folder in os.listdir() if os.path.isdir(folder) and folder not in folders],
              "Archives":[".zip", ".rar", ".7z"],
              "Others": []}


fileExts = [os.path.splitext(i)[1] for i in os.listdir()]
files = {os.path.splitext(i)[0]:os.path.splitext(i)[1] for i in os.listdir() }


for name,ext in files.items():
    for folder, file in extentions.items():
        if ext in file:
            os.replace(f"{name}{ext}", f"{folder}\{name}.{ext}")


for folder in extentions["Folders"]:
    os.replace(f"{folder}", f"Folders\{folder}")


for file in os.listdir():
    if os.path.isfile(file):
        file.replace(f"{file}", f"Others\{file}")

print("Files organized succesfully")