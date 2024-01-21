FROM python:3.11 as build

WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip3 install requests
CMD ["python3", "main.py"]