from urllib.parse import urlparse
import tldextract
import ipaddress
import re

def main_extractor(URL):
    parsed_url = urlparse(URL)
    fqdn = parsed_url.hostname
    tld = tldextract.extract(URL).suffix
    scheme = parsed_url.scheme
    result = [url_length(URL), fqdn_length(URL), is_domain_ip(fqdn), tld_length(tld), subdomain_number(fqdn), obfuscated_chars_number(URL), letter_to_total_ratio(URL), number_to_total_ratio(URL), equal_chars_number(URL), question_mark_chars_number(URL), ampersand_chars_number(URL), other_special_chars_number(URL), whitespace_number(URL), is_https(scheme)] 
    print(result)

def url_length(URL):
    return len(URL)

def fqdn_length(fqdn):
    return len(fqdn)

def is_domain_ip(fqdn):
    try:
        if ipaddress.ip_address(fqdn):
            return 1
    except ValueError:
        return 0

def tld_length(tld):
    return len(tld)

def subdomain_number(fqdn):
    return len(tldextract.extract(fqdn).subdomain.split("."))

def obfuscated_chars_number(URL):
    return len(URL) - len(re.findall(r"[A-Za-z0-9-._~:/?#\[\]@!$&'()*+,;%=]", URL))

def letter_to_total_ratio(URL):
    letters = len(re.findall(r"[a-zA-Z]", URL))
    total_chars = len(URL)
    return letters / total_chars if total_chars > 0 else 0

def number_to_total_ratio(URL):
    numbers = len(re.findall(r"\d", URL))
    total_chars = len(URL)
    return numbers / total_chars if total_chars > 0 else 0

def equal_chars_number(URL):
    return URL.count('=')

def question_mark_chars_number(URL):
    return URL.count('?')

def ampersand_chars_number(URL):
    return URL.count('&')

def other_special_chars_number(URL):
    return len(re.findall(r"[-_~#\[\]@!$'\(\)\*\+,;%]", URL))

def whitespace_number(URL):
    return len(re.findall(r"%20", URL))

def is_https(scheme):
    return int(scheme == "https")

