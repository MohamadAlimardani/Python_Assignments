
from distutils import extension
import os

def Type__of_Files(path_file):
    name , extension = os.path.splitext(path_file)

    print("\nFile Name: " + name + "\nType of File: " + extension)

path_file = input("Enter The Path of You're File: ")

Type__of_Files(path_file)