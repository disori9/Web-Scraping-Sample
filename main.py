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

def send_email():
    print("Email was sent!")

def store(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")

def read_text(txt_file):
    with open(txt_file, "r") as file:
        data = file.readlines()
        data = [info.strip("\n") for info in data]

    return data

if __name__ == "__main__":
    src = scrape(URL)
    value = extract(src)

    tours = read_text("data.txt")

    if value != "No upcoming tours":
        if value not in tours:
            send_email()
            store(value)

    print(tours)
    print(value)