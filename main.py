import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scraping the page source from the URL"""
    response = requests.get(url)
    pg_source = response.text
    return pg_source


if __name__ == "__main__":
    src = scrape(URL)
    print(src)