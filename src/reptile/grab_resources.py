import requests  
  
mine_headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'  
}  
  
def download_resource(url, stored_path):  
    # 发送GET请求获取资源文件  
    response = requests.get(url, headers=mine_headers)  
  
    # 检查响应状态码，确保请求成功  
    if response.status_code == 200:  
        # 将响应内容写入目标文件  
        with open(stored_path, 'wb') as f:  
            f.write(response.content)  
        print(f"The resource file has been successfully saved to: {stored_path}")  
    else:  
        print(f"Request failed with status code: {response.status_code}")  
   