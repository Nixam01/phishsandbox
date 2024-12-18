from collections import defaultdict
import re
import tkinter as tk
from tkinter import filedialog
from email.parser import BytesParser
from email import policy

def load_eml():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select .eml file",
        filetypes=[("EML files", "*.eml")]
    )

    if file_path:
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        return msg
    else:
        print("File was not selected!")
        return None

def parse_headers(msg):
    header_dict = defaultdict(list)
    for key, value in msg.items():
        header_dict[key].append(value)
    return header_dict
    
def parse_body(msg):
    if msg.is_multipart():
        for part in msg.iter_parts():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                return part.get_payload(decode=True).decode(part.get_content_charset())
            elif content_type == 'text/html':
                return part.get_payload(decode=True).decode(part.get_content_charset())
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain':
            return msg.get_payload(decode=True).decode(msg.get_content_charset())
        elif content_type == 'text/html':
            return msg.get_payload(decode=True).decode(msg.get_content_charset())


def extract_ip_and_domains(header_dict):
    IP_addresses = []
    domains = []

    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    domain_pattern = r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    for values in header_dict.items():
        for value in values:
            ip_matches = re.findall(ip_pattern, str(value))
            if ip_matches:
                IP_addresses.extend(ip_matches)
            
            domain_matches = re.findall(domain_pattern, str(value))
            if domain_matches:
                domains.extend(domain_matches)

    return IP_addresses, domains

message = load_eml()
header_dict = parse_headers(message)
body = parse_body(message)

if header_dict:
    for key, value in header_dict.items():
        print(f"{key}: {value}")
    IP_addresses, domains = extract_ip_and_domains(header_dict)
    
    print("IP addresses:", IP_addresses)
    print("Domains:", domains)
print(body)
