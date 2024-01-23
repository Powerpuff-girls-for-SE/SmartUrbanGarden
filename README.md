# SmartUrbanGarden
Smart Urban Garden is a project that leverages the power of IoT to nurture plants within indoor settings. This system aims to streamline gardening efforts by automating essential tasks, conserving water, and ensuring optimal conditions for plant growth. We create an automated ecosystem that employs sensors for monitoring crucial plant parameters such as temperature️, humidity, light levels, and soil moisture.  The primary objective of this system is to significantly reduce manual intervention, enhancing convenience while fostering an ideal environment for plant growth. By continuously storing essential plant data in a relational database, including temperature, humidity, and soil moisture, users gain insights into the conditions necessary for optimal plant health.
This system operates on a processing unit which collect data from various sensors and control actuators. These values will then be displayed on a web dashboard which allows users to know the environmental conditions of the plants when they check on them. The smart urban garden will be divided into areas in which the user can have different plants and conditions for the optimal growth and maintenance of the plant. 

## Execution Steps
1. Download Docker Desktop [link](https://www.docker.com/products/docker-desktop/)
2. Start Docker Desktop
3. Clone this GitHub project and run the following commands:
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

## Sequence Diagram
![sequence diagram drawio](https://github.com/Powerpuff-girls-for-SE/SmartUrbanGarden/assets/46968591/ef7dfd05-28fb-4bc6-8322-0b16a986b5e8)


## MAPE-K Framework
| Component | Description |
| --- | --- |
| Monitor | Monitoring is achieved through various sensors that measure temperature, humidity, light levels, and soil moisture. These sensors continuously gather data about the environmental conditions affecting the plant. |
| Analyser | Analysis involves interpreting the data collected during monitoring. The system analyzes the data from the sensors to determine the current state of the plant's environment. For instance, it assesses whether the soil is too dry or if the ambient light is insufficient. |
| Planner | Planning involves deciding what actions to take based on the analysis. In our smart garden, planning occurs when the system decides whether to water the plant or turn on the light. This decision is based on optimal values for each sensor which are set as part of the system’s logic. |
| Executor | Execution is the act of carrying out the planned actions. In our project, this is done through actuators like the water pump and the Smart Bulb. When the system decides that the plant needs water, it activates the pump; similarly, it turns on the bulb when needed. This ensures that the plant’s environment is always optimal. |
| Knowledge | This aspect involves the information and rules that the system uses to make decisions. Smart Urban Garden uses specific knowledge like the optimal moisture level, light intensity requirements, optimal temperatures for optimal growth of the specific plant. A database with the above thresholds will be created for a variety of plants and shared among the MAPE components. |

## Steps to set up Telegram bot
[Telegram Bot Setup Steps](telegram_bot_setup_steps.pdf)
