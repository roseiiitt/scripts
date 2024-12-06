#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url=sys.argv[1]
proxies = {
    'http': 'http://127.0.0.1:8080',  
    'https': 'http://127.0.0.1:8080'  
}

url=sys.argv[1]
session=requests.Session()


response=session.get(url,proxies=proxies,verify=False)
# find all the <a> tags
soup=BeautifulSoup(response.text,'html.parser')
postid=soup.find_all('a',href=True)

for i in postid:
    href=i['href']
    if 'postId=' in href:
            postid=href
            break
    
print("\n\n\n")
print(postid)


posting_comment_url=f"{url}{postid}"
print("\n",posting_comment_url)

post_request=requests.get(posting_comment_url,proxies=proxies,verify=False)


print("\n Getting csrf token\n")

soup=BeautifulSoup(post_request.text,'html.parser')
csrf_token_tag=soup.find('input',{'name':'csrf'})
csrf_token=csrf_token_tag['value']
print(f"\n{csrf_token}")

form_tag=soup.find_all('form',action=True)
print("\n\n\n",form_tag)
for a in form_tag:
      action=a['action']
      if "/post/comment" in action:
            form_tag=action
            break

final_url=f"{url}{form_tag}"
    
a=postid.split("=")
payload=input("Enter payload:")
name=input("Enter name:")
email=input("Enter email:")
if "@" not in email or email.count("@") != 1:
    print(f"{email} is not a valid email address.")
    sys.exit()
else:
    # Split the email into username and domain
    username, domain = email.split("@")
    
    # Check if the username and domain parts are not empty
    if len(username) == 0 or len(domain) == 0:
        print(f"{email} is not a valid email address.")
    else:
        # Check if the domain contains at least one dot and that the dot is not at the beginning or end
        if "." not in domain or domain.startswith('.') or domain.endswith('.'):
            print(f"{email} is not a valid email address.")
            sys.exit()
        else:
            # Check if the domain part has at least one character before and after the dot
            domain_parts = domain.split(".")
            if len(domain_parts) < 2 or any(len(part) == 0 for part in domain_parts):
                print(f"{email} is not a valid email address.")
                sys.exit()
            else:
                print(f"{email} is a valid email address.")



comment_data={
      'csrf':csrf_token,
      'postId':a[1],
      'comment':payload,
      'name':name,
      'email':email,
      'website':"www.google.com"
}
print(comment_data)

send=session.post(final_url,data=comment_data,proxies=proxies,verify=False)
print(send.text)