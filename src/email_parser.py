from collections import defaultdict
import regex as re
import tkinter as tk
import tldextract
from tkinter import filedialog
from email.parser import BytesParser
from email import policy
from vt_wrapper import check_domain

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
        return body_domains

    if isinstance(object, dict):
        header_domains = []
        for values in object.items():
            for value in values:
                domain_matches = re.findall(domain_pattern1, str(value))
                if domain_matches:
                    header_domains.extend(domain_matches)

        return header_domains

message = load_eml()
header_dict = parse_headers(message)
body = parse_body(message)

if header_dict:
    #for key, value in header_dict.items():
    #    print(f"{key}: {value}")
    header_domains = list(dict.fromkeys(map(str.lower, extract_domains(header_dict))))
    body_domains = list(dict.fromkeys(map(str.lower, extract_domains(body))))
    
for domain in body_domains:
    domain_analysis_results = {}
    tld = tldextract.extract(domain).suffix
    length = len(domain)
    subdomains = len(tldextract.extract(domain).subdomain.split("."))
    is_ascii = domain.isascii()
    domain_creation_date, malicious_hits, is_certificate_valid = check_domain(domain)
    domain_analysis_results[domain] = {
            "tld": tld,
            "length": length,
            "subdomains": subdomains,
            "is_ascii": is_ascii,
            "domain_creation_date": domain_creation_date,
            "malicious_hits": malicious_hits,
            "is_certificate_valid": is_certificate_valid
        }
    print(domain_analysis_results)

print("Domains in header:", header_domains)
print("Domains in body:", body_domains)
