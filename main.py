import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scraping the page source from the URL"""
    response = requests.get(url)
    pg_source = response.text
    return pg_source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted_value = extractor.extract(source)["tours"]
    return extracted_value

if __name__ == "__main__":
    src = scrape(URL)
    value = extract(src)
    print(value)