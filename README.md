# SmartUrbanGarden
Smart Urban Garden is a project that leverages the power of IoT to nurture plants within indoor settings. This system aims to streamline gardening efforts by automating essential tasks, conserving water, and ensuring optimal conditions for plant growth. We create an automated ecosystem that employs sensors for monitoring crucial plant parameters such as temperature️, humidity, light levels, and soil moisture.  The primary objective of this system is to significantly reduce manual intervention, enhancing convenience while fostering an ideal environment for plant growth. By continuously storing essential plant data in a relational database, including temperature, humidity, and soil moisture, users gain insights into the conditions necessary for optimal plant health.
This system operates on a processing unit which collect data from various sensors and control actuators. These values will then be displayed on a web dashboard which allows users to know the environmental conditions of the plants when they check on them. The smart urban garden will be divided into areas in which the user can have different plants and conditions for the optimal growth and maintenance of the plant. 
<img width="50%" alt="image" src="https://github.com/Powerpuff-girls-for-SE/SmartUrbanGarden/assets/46968591/e9a0b07e-55f3-4b60-8a23-e7d4e318bd82">

## Execution Steps
```bash
docker-compose build
docker-compose up
```

## Functional Requirements
| Requirement Name             | Description |
| ---------------------------- | ----------- |
| Intelligent Watering Mechanism | Utilizes soil moisture sensors to regulate watering, ensuring efficient use of water resources. |
| Intelligent Light Adjustment  | Utilizes light sensors to regulate light intensity, ensuring efficient use of light resources. |
| Intelligent Heating Regulation | Utilizes temperature sensors to regulate thermostat, ensuring efficient use of heating resources. |
| Intelligent Humidity Regulation | Utilizes humidity sensors to regulate humid level, ensuring efficient use of Humidifier. |
| Automated Plant Care | Automates routines like watering and light adjustments based on plant needs, reducing manual care. |
| Remote Monitoring System | Offers a web-based interface for users to monitor real-time data on lighting, temperature, moisture, and humidity levels suitable for plant growth. |
| Alert System | Offers user text-based alert on Telegram if some sensor values record values beyond the threshold. |

## Managed Resources
| Managed Resource   | Sensors             | Actuators   |
| ------------------ | ------------------- | ----------- |
| Watering System    | Soil Moisture sensor | Water Pump  |
| Humidity Regulator | Humidity sensor     | Humidifier  |
| Lighting System    | Light sensor        | Smart Bulb  |
| Heating System     | Temperature Sensor  | Thermostat  |

## System Architecture
<img width="50%" alt="image" src="https://github.com/Powerpuff-girls-for-SE/SmartUrbanGarden/assets/46968591/3013f515-5316-4bb6-b5f6-610dc04c3cda">



