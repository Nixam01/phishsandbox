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
def check_domain(domain):
    try:
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response

        # Print the JSON response in a pretty format
        #print("Full Response:")
        #print(json.dumps(data, indent=4))

        # Extract and print last_analysis_stats
        #last_analysis_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        #print("\nLast Analysis Stats:")
        #print(json.dumps(last_analysis_stats, indent=4))

        #malicious_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", {})
        #print("\nMalicious Stats:")
        #print(json.dumps(malicious_stats, indent=4))

        #if (malicious_stats > 4):
        #    print(f"Domain {domain} is malicious")
        #else:
        #    print(f"Domain {domain} is not malicious")

        domain_creation_date = data.get("data", {}).get("attributes", {}).get("creation_date")
        malicious_hits = data.get("data", {}).get("attributes", {}).get("total_votes", {}).get("malicious")
        now = datetime.now()
        not_valid_before = datetime.strptime(data.get("data", {}).get("attributes", {}).get("last_https_certificate", {}).get("validity", {}).get("not_before"), "%Y-%m-%d %H:%M:%S")
        not_valid_after = datetime.strptime(data.get("data", {}).get("attributes", {}).get("last_https_certificate", {}).get("validity", {}).get("not_after"), "%Y-%m-%d %H:%M:%S")
        is_certificate_valid = not_valid_before <= now <= not_valid_after


        return domain_creation_date, malicious_hits, is_certificate_valid


    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None, None
def main():

    domain = input("Enter the domain you want to check: ")
    check_domain(domain)

if __name__ == "__main__":
    main()