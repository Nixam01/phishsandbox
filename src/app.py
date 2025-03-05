from email_parser import parse_email
from feature_extractor import main_extractor
from model_training import predict_domain
from vt_wrapper import domain_hits

input('Press ENTER to load an .eml file')

urls = parse_email()

for url in urls:
    features = main_extractor(url)
    predict_domain(features, url)
    print("VirusTotal hits: " + str(domain_hits(url)))