import requests
from selectorlib import Extractor

r = requests.get('https://www.timeanddate.com/weather/kyrgyzstan/bishkek')
c = r.text

extractor = Extractor.from_yaml_file('../logic/temperature.yaml')
a = (extractor.extract(c))
a = float(a['temp'].replace('\xa0°C', ''))
print(a)
