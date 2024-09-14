import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext)
            if not os.path.exists(folder):
                os.makedirs(folder)
            shutil.move(file_path, os.path.join(folder, filename))

directory = input("Enter the directory path to organize: ")
organize_files(directory)
print("Files have been organized.")
