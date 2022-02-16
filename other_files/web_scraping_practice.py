import requests
from selectorlib import Extractor

r = requests.get('https://www.timeanddate.com/worldclock/usa/new-york')
c = r.text

extractor = Extractor.from_yaml_file('current_time.yaml')
print(extractor.extract(c))
