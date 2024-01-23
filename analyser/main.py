import numpy
import requests
import traceback
import configparser
from time import sleep

import db_access
from get_optimal_values import get_optimal_value

config = configparser.ConfigParser()
config.read('config.ini')

def main():
    try:
        connection = db_access.DBAccess()
        garden_areas = connection.get_garden_areas()
        used_sensors = ["light", "temperature", "humidity", "moisture"]
        sensor_data = {}

        for garden_area in garden_areas:
            garden_area_values = {}
            for sensor in used_sensors:
                value = connection.get_values_from_database(garden_area, sensor)
                garden_area_values[sensor] = value

            sensor_data[garden_area] = garden_area_values

        readings = check_sensor_values(sensor_data)
        url = 'http://172.100.0.16:5007/planner/check_measurements'
        requests.post(url, json=readings)

    except Exception as exc:
        traceback.print_exc()

def check_temperature_value(garden_area, temperature):
    optimal_temperature = get_optimal_value(garden_area, "temperature")
    if temperature < optimal_temperature - 5:
        return "Temperature low"
    elif temperature > optimal_temperature + 5:
        return "Temperature high"
    else:
        return "Temperature optimal"

def check_humidity_value(garden_area, humidity):
    optimal_humidity = get_optimal_value(garden_area, "humidity")
    if humidity < optimal_humidity - 5:
        return "Humidity low"
    elif humidity > optimal_humidity + 5:
        return "Humidity high"
    else:
        return "Humidity optimal"
    
def check_light_value(garden_area, light):
    optimal_light = get_optimal_value(garden_area, "light")
    if light < optimal_light - 5:
        return "Light low"
    elif light > optimal_light + 5:
        return "Light high"
    else:
        return "Light optimal"
    
def check_moisture_value(garden_area, moisture):
    optimal_moisture = get_optimal_value(garden_area, "moisture")
    if moisture < optimal_moisture - 5:
        return "Moisture low"
    elif moisture > optimal_moisture + 5:
        return "Moisture high"
    else:
        return "Moisture optimal"
    
def check_sensor_values(sensor_data):
    readings = {}
    for garden_area, values in sensor_data.items():
        readings[garden_area] = {}
        for sensor, value in values.items():
            averaged_value = numpy.mean(list(sensor_data[garden_area][sensor].values()))
            if sensor == 'light':
                readings[garden_area]["light"] = check_light_value(garden_area, averaged_value)
            elif sensor == 'temperature':
                readings[garden_area]["temperature"] = check_temperature_value(garden_area, averaged_value)
            elif sensor == 'moisture':
                readings[garden_area]["moisture"] = check_moisture_value(garden_area, averaged_value)
            elif sensor == 'humidity':
                readings[garden_area]["humidity"] = check_humidity_value(garden_area, averaged_value)

    return readings

if __name__ == "__main__":
    while True:
        main()
        sleep(10)