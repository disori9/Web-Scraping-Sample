import requests
import selectorlib
import time
import sqlite3
from send_email import send_email

connection = sqlite3.connect("data.db")
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

def store(extracted_data):
    tour_info = extracted_data.split(",")
    tour_info = [info.strip() for info in tour_info]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", tour_info)
    connection.commit()

def read_data(extracted_data):
    tour_info = extracted_data.split(",")
    tour_info = [info.strip() for info in tour_info]
    band, city, date = tour_info
    cursor = connection.cursor()
    # basically, this will return a list of tuple if there is already a band with the same information in the db
    # otherwise it returns nothing
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
     while True:
        src = scrape(URL)
        value = extract(src)
        print(value)
        if value != "No upcoming tours":
            tours = read_data(value)
            print(tours)
            # here, we check if there is already a row in the db with the same info, if there is none (see read_data)
            # returned, we store that info in the database and send an email, otherwise, the if condition doesn't
            # start
            if not tours:
                send_email(value)
                store(value)
        print(value)
        time.sleep(2)