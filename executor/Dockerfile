FROM python:3.11 as build

WORKDIR /app
COPY . .

RUN pip3 install influxdb-client
RUN pip3 install tenacity
RUN pip3 install paho-mqtt
RUN pip3 install Flask
RUN pip3 install requests

CMD ["python3", "main.py"]