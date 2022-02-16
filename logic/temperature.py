import requests
from selectorlib import Extractor


class Temperature:
    """
    Gets the temperature of user location by using the information(country,city)
    and using web srcaping technique. The web page will be (timeanddate.com/weather)
    """

    base_url = 'https://www.timeanddate.com/weather/'
    yal_path = 'logic/temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace("", "-")
        self.city = city.replace("", "-")

    def _build_url(self):
        """
        Building the url.
        """
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """
        Scraping the webpage
        """
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yal_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract((full_content))
        return raw_content

    def get(self):
        """
        Cleaning the scrape result
        """
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('°C', '').strip())  # strip method to removes empty spaces


