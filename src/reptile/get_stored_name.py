import os

def get_file_name(url,res_directory):
  file_name = url.split('/')[-1]
  stored_name=str(res_directory)+os.sep+file_name  
  
  print('\n-stored_name: '+stored_name)
  return stored_name