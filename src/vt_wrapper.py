import requests
import json
from datetime import datetime


# Replace 'your-api-key' with your actual VirusTotal API key
# with open('api.key', 'r') as file:
#     API_KEY = file.read()

API_KEY = "6ad968cbce66bc137d7f2dc51edfbd87834aad5839ab6263ef4a814d6968acf4"

headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}
def domain_hits(domain):
    try:
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Print the JSON response in a pretty format
        #print("Full Response:")
        #print(json.dumps(data, indent=4))

        # Extract and print last_analysis_stats
        #last_analysis_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        #print("\nLast Analysis Stats:")
        #print(json.dumps(last_analysis_stats, indent=4))

        malicious_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", {})
        return malicious_stats
        #print("\nMalicious Stats:")
        #print(json.dumps(malicious_stats, indent=4))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None, None
