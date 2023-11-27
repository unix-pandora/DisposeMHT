import os

def writing_into_txt(output_path, content):  
    # 如果文件不存在，则创建文件  
    if not os.path.exists(output_path):  
        with open(output_path, 'w') as f:  
            f.write('')  
  
    # 覆盖写入内容  
    with open(output_path, 'w') as f:  
        f.write(content)