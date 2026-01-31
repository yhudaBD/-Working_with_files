import os

def print_fils_py(path):
  result =[]

  for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
      if full_path.endswith(".py"):
        result.append(full_path)
    else:
      result.extend(print_fils_py(full_path))  
  return result
files = print_fils_py(r"C:\Users\User\Desktop\Working_with_files")
print(files)
 
