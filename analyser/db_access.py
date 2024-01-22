import requests
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from tenacity import retry
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class DBAccess:
    def __init__(self):
        self.organization = config["influxdb"]["ORG"]
        self.bucket = config["influxdb"]["BUCKET_NAME"]
        self.token = config["influxdb"]["TOKEN"]
        self.influxdb_url = config["influxdb"]["URL"]
        self.url = f"http://172.100.0.11:8086"
        self.connect_to_database()

    def connect_to_database(self):
        self.client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.organization)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def get_garden_areas(self):
        query_api = self.client.query_api()
        query = f'import "influxdata/influxdb/schema" schema.tagValues(bucket: "{self.bucket}", tag: "garden_area")'
        results = query_api.query(org=self.organization, query=query)

        garden_area_names = []
        for element in results.to_values():
            garden_area_names.append(list(element)[2])

        return garden_area_names
    
    def get_values_from_database(self, garden_area, sensor):
        query_api = self.client.query_api()
        # query = f'from(bucket: "{self.bucket}") |> range(start: -5m)  |> filter(fn: (r) => r["_measurement"] == "garden")  ' \
        #         f'|> filter(fn: (r) => r["garden_area"] == "{garden_area}")  |> filter(fn: (r) => r["_field"] == "{sensor}")  ' \
        #         f'|> yield(name: "last")'
        query = f'from(bucket:"' + self.bucket + '") |> range(start: -5m) |> filter(fn: (r) => r["_measurement"] == "garden")'
        query_result = query_api.query(org=self.organization, query=query)

        values = {}
        for value in json.loads(query_result.to_json()):
            values[value['_time']] = value['_value']

        return values
