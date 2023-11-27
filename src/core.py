import os
import sys
sys.path.append('./src/api')
sys.path.append('./src/reptile')

import get_mht
import parse2htm
import writing_into
import build_path
import extract_values
import grab_resources
import get_stored_name
import get_matches_files
import write_list_txt

mht_file_directory = "F:\\XNG\\FLV\\offline"
output_htm_folder = 'F:\\XNG\\FLV\\htm'
store_res_dir = 'F:\\XNG\\FLV\\img'
txt_path="F:\\XNG\\FLV\\url-list.txt"

class_name = 'VM_JIY'
extension_name = '.mht'
 
def operate(file_name,class_name):
  saved_htm_path = build_path.get_new_f_name(file_name,output_htm_folder)
  
  mht_cont=get_mht.get_mht(file_name)
  html_content=parse2htm.parse_2_html(file_name,mht_cont)
  
  writing_into.writing_into_txt(saved_htm_path, str(html_content))
  
  values = extract_values.extract_hrefs_from_html(saved_htm_path, class_name)
  return values

def index(mht_file_name):
  url_list = operate(mht_file_name,class_name) 
  
  write_list_txt.write_elements_to_file(url_list,txt_path)
  
  # for url in url_list:
  #   new_file_path = get_stored_name.get_file_name(url,store_res_dir)
  #   grab_resources.download_resource(url,new_file_path)

def pivot(): 
  file_name_list = get_matches_files.get_files_with_extension(mht_file_directory,extension_name)
    
  for file_name in file_name_list:
    index(file_name)
  
pivot()  