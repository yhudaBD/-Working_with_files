import os

def End_count(path):
  result = {}

  for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
      if "." in item:
       ext = item.split(".")[-1]
       if ext in result:
        result[ext] +=1
       else:
        result[ext] = 1
    else:
     sub_res = End_count(full_path)
    
     for key in sub_res:
       if key in result:
        result[key] += sub_res[key]
       else:
         result[key] = sub_res[key]
  return result    
files =End_count(r"C:\Users\User\Desktop\Working_with_files")
print(files)
 
