# https://www.google.com/maps/timeline/kml?authuser=0&pb=!1m8!1m3!1i2020!2i5!3i8!2m3!1i2020!2i5!3i8
from datetime import datetime
from dateutil.rrule import rrule, DAILY
from http.cookies import SimpleCookie
import requests


if __name__ == '__main__':
    print("This script will download your Google Maps Timeline as KML files, one file per day.\n")

    cookie_string = input("We now must obtain the cookies.\n\
    1. Visit https://timeline.google.com/maps/timeline in your browser\n\
    2. In the \"Network\" tab of the DevTools right click on the \"timeline\" document in the list\n\
    3. Under \"Copy\" select \"Copy as cURL\"\n\
    4. Paste it into a text editor and then select and copy the value of the \"cookie\" header\n\
    5. Paste that value here:")
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    start_string = input("Enter the first date you would like to export (in YYYY-MM-DD format): ")
    start_date = datetime.strptime(start_string, "%Y-%m-%d")

    end_string = input("Enter the last date you would like to export (in YYYY-MM-DD format): ")
    end_date = datetime.strptime(end_string, "%Y-%m-%d")

    for dt in rrule(DAILY, dtstart=start_date, until=end_date):
        url = "https://www.google.com/maps/timeline/kml?authuser=0&pb=!1m8!1m3!1i{y}!2i{m}!3i{d}!2m3!1i{y}!2i{m}!3i{d}".format(
            y=dt.year,
            m=dt.month - 1,
            d=dt.day
        )
        r = requests.get(url, cookies=cookies)
        r.raise_for_status()
        file_path = '/usr/local/bin/kmls/history-{0}.kml'.format(dt.strftime("%Y-%m-%d"))
        with open(file_path, 'wb') as f:
            f.write(r.content)
