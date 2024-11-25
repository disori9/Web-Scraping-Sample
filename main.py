import requests
import selectorlib
import time
from send_email import send_email

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

def store(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")

def read_text(txt_file):
    with open(txt_file, "r") as file:
        data = file.readlines()
        data = [info.strip("\n") for info in data]

    return data

if __name__ == "__main__":
     while True:
        src = scrape(URL)
        value = extract(src)

        tours = read_text("data.txt")

        if value != "No upcoming tours":
            if value not in tours:
                send_email(value)
                store(value)
        print(value)
        time.sleep(2)