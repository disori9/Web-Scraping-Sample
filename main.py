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
    with open("data.txt", "r") as file:
        extracted_data = file.readlines()

    with open("data.txt", "w") as file:
        extracted_data.append(data + "\n")
        file.writelines(extracted_data)

if __name__ == "__main__":
    src = scrape(URL)
    value = extract(src)

    with open("data.txt", "r") as file:
        tours = file.readlines()
        tours = [tour.strip("\n") for tour in tours]

    if value != "No upcoming tours":
        if value not in tours:
            send_email()
            store(value)

    print(tours)
    print(value)