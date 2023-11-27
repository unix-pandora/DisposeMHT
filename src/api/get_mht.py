def get_mht(file_name):
  with open(file_name, 'rb') as f:
    mht_content = f.read()
    return mht_content.decode('utf-8')  # 将二进制数据解码为字符串 