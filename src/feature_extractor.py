from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import tldextract
import ipaddress
import re

def main_extractor(URL):
    driver = webdriver.Chrome()
    driver.get(URL)
    page_source = driver.page_source
    parsed_url = urlparse(URL)
    fqdn = parsed_url.hostname
    tld = tldextract.extract(URL).suffix
    scheme = parsed_url.scheme
    result = [url_length(URL), fqdn_length(URL), is_domain_ip(fqdn), tld_length(tld), subdomain_number(fqdn), obfuscated_chars_number(URL), letter_to_total_ratio(URL), number_to_total_ratio(URL), equal_chars_number(URL), question_mark_chars_number(URL), ampersand_chars_number(URL), other_special_chars_number(URL), whitespace_number(URL), is_https(scheme)] 
    print(result)
    driver.quit()

# URL features:

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


# HTML features: 


def has_title(driver):
    return int(len(driver.find_elements(By.TAG_NAME, "title")) > 0)

def has_robots(driver):
    return int(len(driver.find_elements(By.XPATH, "//meta[@name='robots']")) > 0)

def has_icon(driver):
    return int(len(driver.find_elements(By.XPATH, "//link[@rel='icon']")) > 0)

def number_of_redirections(driver):
    clickable_links = 0
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        if link.is_displayed():
            clickable_links += 1
    return clickable_links

def has_description(driver):
    return int(len(driver.find_elements(By.XPATH, "//meta[@name='description']")) > 0)

def number_of_popups(driver):
    return driver.page_source.lower().count("window.open")

def number_of_iframes(driver):
    return len(driver.find_elements(By.TAG_NAME, "iframe"))

def number_of_form_submits(driver):
    return len(driver.find_elements(By.TAG_NAME, "form"))

def has_submit_button(driver):
    return int(len(driver.find_elements(By.XPATH, "//input[@type='submit']")) + len(driver.find_elements(By.XPATH, "//button[@type='submit']")) > 0)

def has_hidden_fields(driver):
    return int(len(driver.find_elements(By.XPATH, "//input[@type='hidden']")) > 0)

def has_password_field(driver):
    return int(len(driver.find_elements(By.XPATH, "//input[@type='password']")) > 0)

def has_bank_reference(driver):
    return driver.page_source.lower().count("bank")

def has_pay_reference(driver):
    return driver.page_source.lower().count("pay")

def has_crypto_reference(driver):
    return driver.page_source.lower().count("crypto")

def number_of_images(driver):
    return len(driver.find_elements(By.TAG_NAME, "img"))

def number_of_css_references(driver):
    link_css_count = len(driver.find_elements(By.XPATH, '//link[@rel="stylesheet"]'))
    style_css_count = len(driver.find_elements(By.TAG_NAME, 'style'))
    inline_css_count = len(driver.find_elements(By.XPATH, '//*[@style]'))
    total_css_references = link_css_count + style_css_count + inline_css_count
    return total_css_references

def number_of_js_references(driver):
    script_js_count = len(driver.find_elements(By.TAG_NAME, 'script'))
    js_event_attributes = [
        'onclick', 'onmouseover', 'onload', 'onchange', 'onsubmit', 'onkeydown', 
        'onkeyup', 'onfocus', 'onblur', 'onselect', 'onerror']
    js_event_count = 0
    for attr in js_event_attributes:
        js_event_count += len(driver.find_elements(By.XPATH, f'//*[@{attr}]'))
    total_js_references = script_js_count + js_event_count
    return(total_js_references)