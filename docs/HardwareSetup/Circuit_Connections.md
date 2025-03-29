# Raspberry Pi Circuit Connections

This document provides details on the pin connections of the Raspberry Pi to the BMP280, DHT22, and LCD display with the PCF8574 expander.

## Components Used
- **Raspberry Pi (Any Model with GPIO support)**
- **BMP280 Sensor** (Barometric Pressure & Temperature Sensor)
- **DHT22 Sensor** (Temperature & Humidity Sensor)
- **16x2 LCD Display with PCF8574 I2C Expander**

## Pin Connections

### **Raspberry Pi to BMP280**
| BMP280 Pin | Raspberry Pi Pin |
|------------|-----------------|
| VCC        | 3.3V (Pin 1)    |
| GND        | GND (Pin 6)     |
| SCL        | GPIO3 (SCL - Pin 5) |
| SDA        | GPIO2 (SDA - Pin 3) |

### **Raspberry Pi to DHT22**
| DHT22 Pin | Raspberry Pi Pin |
|------------|-----------------|
| VCC        | 3.3V or 5V (Pin 1 or 2) |
| GND        | GND (Pin 6)     |
| DATA       | GPIO4 (Pin 7)   |


### **Raspberry Pi to LCD (via PCF8574)**
| PCF8574 Pin | Raspberry Pi Pin |
|------------|-----------------|
| VCC        | 5V (Pin 4)      |
| GND        | GND (Pin 6)     |
| SDA        | GPIO2 (SDA - Pin 3) |
| SCL        | GPIO3 (SCL - Pin 5) |

## Notes
- The BMP280 and LCD (via PCF8574) communicate using I2C.
- Enable I2C on Raspberry Pi using `sudo raspi-config`.
- Install required libraries for communication:
  ```sh
  sudo apt-get install python3-smbus i2c-tools
  pip install Adafruit-BMP280 Adafruit-DHT
  ```

This setup ensures proper interfacing between the sensors, display, and Raspberry Pi using I2C and GPIO communication.
