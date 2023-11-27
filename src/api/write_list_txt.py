import os

def write_elements_to_file(ele_list, txt_path):  
    # 如果文件不存在，创建文件  
    if not os.path.exists(txt_path):  
        with open(txt_path, 'w') as f:  
            f.write('')  
  
    # 循环ele_list，将每个元素写入文件  
    with open(txt_path, 'a') as f:  
        for ele in ele_list:  
            f.write(ele + '\n')