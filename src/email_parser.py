from collections import defaultdict
from urllib.parse import urlparse
import regex as re
import tkinter as tk
import requests
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


def extract_domains(object):

    domain_pattern1 = r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    domain_pattern2 = r'(?<=https?:\/\/)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    if isinstance(object, str):
        body_domains = []
        body_domains.extend(re.findall(domain_pattern2, object))
        return list(set(body_domains))

    if isinstance(object, dict):
        header_domains = []
        for values in object.items():
            for value in values:
                domain_matches = re.findall(domain_pattern1, str(value))
                if domain_matches:
                    header_domains.extend(domain_matches)
        return list(set(header_domains))
    
def check_protocol(domains):
    urls = []
    for domain in domains:
        try:
            r = requests.get(domain)
            urls.append(r.url)
        except:
            try:
                r = requests.get('https://' + domain)
                urls.append(r.url)
            except:
                try:
                    r = requests.get('http://' + domain)
                    urls.append(r.url)
                except:
                    print("Cannot connect to " + domain)
    return urls

def parse_email():
    message = load_eml()
    body = parse_body(message)
    body_domains = extract_domains(body)
    urls = check_protocol(body_domains)
    return urls



