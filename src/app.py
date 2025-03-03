from email_parser import parse_email
from feature_extractor import main_extractor
from model_training import predict_domain
from vt_wrapper import domain_hits

input('Press ENTER to load an .eml file')

urls = parse_email()
print(urls)

for url in urls:
    features = main_extractor(url)
    predict_domain(features)
    print(domain_hits(url))


