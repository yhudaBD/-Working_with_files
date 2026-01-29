import os

def print_fils(path):
  for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
      print(full_path)
    else:
      print_fils(full_path)  
    
print_fils(r"C:\Users\User\Desktop\Working_with_files")  
