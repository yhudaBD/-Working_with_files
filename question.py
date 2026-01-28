import os

os.chdir(r"C:\Users\User\Desktop\Working_with_files\test")
print(os.listdir())
os.chdir("..")
print(os.getcwd())