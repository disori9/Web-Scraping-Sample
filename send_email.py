import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    tour_info = message.split(",")
    band = tour_info[0]
    place = tour_info[1]
    date = tour_info[2]

    message = f"""\
Subject: New Upcoming Tour from: {band}

Where: {place}
When: {date}"""

    username = "violetori99@gmail.com"
    password = "adgm brzf nocs zykc"

    receiver = "violetori99@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
