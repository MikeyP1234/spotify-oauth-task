import requests
import json

# Set the POST data
data = {
    'grant_type': 'client_credentials',
    'client_id': 'removed',
    'client_secret': 'removed'
}

# Set headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Make the POST request
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
# Print the result
r_dict = response.json()
m = r_dict['access_token']

# Replace with your actual token (usually you get this from the token endpoint)
access_token = m

# Set up the headers
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Spotify artist endpoint
url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"

# Make the GET request
response = requests.get(url, headers=headers)

# Check the result
if response.status_code == 200:
    with open("data.json","w") as file:
        data = response.json()
        json.dump(data,file,indent=4)
else:
    print(f"Error {response.status_code}: {response.text}")
