# Raspberry Pi Weather Station

## Overview
This project is a Raspberry Pi-based weather station that measures and displays real-time environmental data. It uses various sensors to collect weather-related data and uploads it to a ThingSpeak channel for remote monitoring.

## Features
- **Real-time Display:** Shows data on a 16x2 LCD display.
- **Sensors Used:**
  - BMP280: Measures atmospheric pressure.
  - DHT22: Measures temperature and humidity.
- **Cloud Integration:** Data is uploaded to a ThingSpeak channel.
- **Future Enhancements:** Planned integration of dust and gas sensors.

## Components Required
- Raspberry Pi 4
- 16x2 LCD Display
- BMP280 Sensor (Pressure)
- DHT22 Sensor (Temperature & Humidity)
- Jumper wires
- Breadboard (optional)

## Hardware Setup
![Hardware Setup](images/hardware_setup.jpg)

## ThingSpeak View
![ThingSpeak View](images/thingspeak_display.jpg)

## Folder Structure
```
RaspberryPi-WeatherStation/
│── src/                      # Python script
│── docs/                     # Documentation
│── images/                   # Project images
│── requirements.txt          # List of required Python libraries
│── README.md                 # Project details
│── .gitignore                # Ignore unnecessary files
```

## Tags
- Raspberry Pi
- Weather Station
- IoT
- ThingSpeak
- Environmental Monitoring
