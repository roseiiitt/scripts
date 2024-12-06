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

url = sys.argv[1]
print(url)

response = requests.get(url,proxies=proxies,verify=False)
print(response.text)

endpoint="/?search="
payloads=input("Enter payload:")

final_url=f"{url}{endpoint}{payloads}"
print(final_url)
res=requests.get(final_url,proxies=proxies,verify=False)

time.sleep(4)
soup=BeautifulSoup(res.text, 'html.parser')

completed =soup.find('h4').text
print(completed)
