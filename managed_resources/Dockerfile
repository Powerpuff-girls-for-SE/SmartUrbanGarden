FROM python:3.11 as build
WORKDIR /app
COPY . .

RUN pip install paho-mqtt
RUN pip install pandas

CMD ["python3", "main.py"]