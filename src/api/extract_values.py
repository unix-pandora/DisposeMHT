from bs4 import BeautifulSoup  
import os  
  
def extract_hrefs_from_html(html_file_path, class_name):  
    # 检查文件是否存在  
    if not os.path.isfile(html_file_path):  
        raise FileNotFoundError("The file does not exist: {}".format(html_file_path))  
  
    with open(html_file_path, 'r', encoding='utf-8') as f:  
        soup = BeautifulSoup(f.read(), 'html.parser')  
  
    # 找到所有类名为 class_name 的标签  
    tags = soup.find_all(class_=class_name)  
  
    # 提取每个标签的href属性值，存入列表  
    href_values = [tag['href'] for tag in tags if 'href' in tag.attrs]
      
    print('\n-href_values: '+str(href_values))
    return href_values