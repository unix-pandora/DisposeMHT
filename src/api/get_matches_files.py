import os  
  
# 遍历指定文件夹并筛选出具有特定扩展名的文件 
def get_files_with_extension(dir_name, extension_type):  
    result = []  
    for root, dirs, files in os.walk(dir_name):  
        for file in files:  
            if file.endswith(extension_type):  
                result.append(os.path.join(root, file))  
    print('\n-get_files_with_extension: '+str(result))                
    return result