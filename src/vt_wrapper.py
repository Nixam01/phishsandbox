import requests
import json

# Replace 'your-api-key' with your actual VirusTotal API key
with open('api.key', 'r') as file:
    API_KEY = file.read()
DOMAIN = "example.com"  # Replace with the domain you want to check

# Set the API endpoint and headers
url = f"https://www.virustotal.com/api/v3/domains/{DOMAIN}"
headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

# Perform the GET request
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()  # Parse the JSON response

    # Print the JSON response in a pretty format
    print(json.dumps(data, indent=4))
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
