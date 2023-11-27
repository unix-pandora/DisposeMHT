import os

def get_new_f_name(f_name,out_path):
  file_name = get_previous_name(f_name)
  print('\n-file_name: '+file_name)
  
  file_name = file_name.replace(' ', '-')
  output_html = out_path+str(os.sep)+file_name+'.html'
  print('\n-output_html: '+output_html)
  return output_html
  
def get_previous_name(url_str):  
    # 按地址分隔符进行截取，得到一个数组  
    path_parts = os.path.split(url_str)
    name_arr = str(path_parts[1]).split('.')
    # 数组中的最后一个元素  
    return name_arr[0]  
     