import os
for FolderNames, SubFolders, FilelNames in os.walk(r"D:\Prof_Seemo"):
    print(f"The Folder is {FolderNames}")
    print(f"The Subfolders in {FolderNames} are {SubFolders}")
    print(f"The File Names in {FolderNames} are {FilelNames}")
    print("##############################################################")
