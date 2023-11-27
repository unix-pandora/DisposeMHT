import email

def parse_2_html(file_name,mht_content):
  html_content = ''
  
  mht_message = email.message_from_string(mht_content)
  for part in mht_message.walk():
    content_type = part.get_content_type()
    if content_type == 'text/html':
        html_content = part.get_payload(decode=True)
        break
  return html_content