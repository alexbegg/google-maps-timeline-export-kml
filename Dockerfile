FROM python:3.6.10-slim

COPY . /usr/local/bin

WORKDIR /usr/local/bin

RUN pip install -r requirements.txt

CMD ["python", "google_maps_timeline_export_as_kml.py"]
