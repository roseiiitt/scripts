import requests
from bs4 import BeautifulSoup
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time

url=sys.argv[1]
username = input("Enter username:")
password = sys.argv[2]
print (url)
proxies = {
    'http': 'http://127.0.0.1:8080',  
    'https': 'http://127.0.0.1:8080'  
}

session=requests.Session()


#csrf_token

response=session.get(url,proxies=proxies,verify=False)
if response.status_code != 200:
    print(f"Failed to retrieve the login page. Status code: {response.status_code}")
    sys.exit()

soup=BeautifulSoup(response.text,'html.parser')

csrf_token=soup.find('input',{'name':'csrf'})
print(f"\ncsrf_token{csrf_token}")
if not csrf_token:
    print("\n Failed to fetch the csrf token")

else:
    csrf_token_value = csrf_token['value']
    print(csrf_token_value)

login_data={
    'csrf':csrf_token_value,
    'username':username,
    'password':password
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

send=session.post(url,data=login_data,headers=headers,proxies=proxies,verify=False)
print("\n",login_data)


time.sleep(3)
soup = BeautifulSoup(send.text, 'html.parser')
completed = soup.find('h4')

valid=soup.find('a',href="/logout")
if valid:
    print("\nLogged in as admin:")
    if completed:
	    print("\n",completed.text)

else:
    print("\nNot logged in as admin:")
          
