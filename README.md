# Google Maps Timeline Export as KML

A Python script that exports the Google Maps Timeline data for each day in a date range as KML files.

Inspired by https://community.alteryx.com/t5/Alteryx-Designer-Discussions/Download-Google-Maps-Timeline-Data-with-all-Details/td-p/521944

## WARNING

This is an experiment and has no rate limiting. Exporting out approximately 50+ files (days) will run into an error regarding too many requests.

## Better alternative

A better alternative is to download all of your "Location History" from Google Takeout: https://takeout.google.com/settings/takeout/custom/location_history. The download will have your history, one JSON file for each month.

## Run this with docker

```shell
cd google_maps_timeline_export_as_kml
docker build -t google_maps_timeline_export_as_kml . 
docker run -it --rm -v "$(pwd)"/kmls:/usr/local/bin/kmls google_maps_timeline_export_as_kml
```
