# Tool to get the /robots.txt file (if exists) from a website
import requests

user_rl = str(input("Enter the full URL: "))
split_user_url = list(user_rl)

# print(split_user_url) # DEBUGG

# Format the url 'correctly' for the '/robots.txt' chain directory
if split_user_url[-1] == '/':
    split_user_url[-1].replace('/', '') # remove the last '/' if the user URL contains it

user_url_robots = ''.join(split_user_url) + '/robots.txt'

# Send a request to the website to check if the directory */robots.txt exists
try:
    response = requests.get(user_url_robots, timeout=5)
    if response.status_code == 200:
        print("Directory exists! | Data Fetched")
        robots_data = response.text # Robots.txt content

    elif response.status_code == 403:
        print("Directory exists but access is forbidden.")
    elif response.status_code == 404:
        print("Directory does not exist.")
    else:
        print(f"Received unexpected status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")


print(robots_data)
