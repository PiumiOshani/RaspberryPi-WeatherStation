import time
import board
import busio
import adafruit_bmp280
from RPLCD.i2c import CharLCD
import smbus2 as smbus
import adafruit_dht
import requests 

# ThingSpeak Configuration
THINGSPEAK_API_KEY = 'B0WA0LMKQLYQZTUP'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

# Define constants and setup
# For BMP280 sensor
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Set sea level pressure for altitude calculation 
bmp280.sea_level_pressure = 1008 # Standard pressure in hPa

# For DHT22 Sensor
dht_device = adafruit_dht.DHT22(board.D4)

# For LCD Display
LCD_ADDRESS = 0x27 
LCD_COLS = 16
LCD_ROWS = 2

# Initialize the LCD
lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDRESS, cols=LCD_COLS, 
              rows=LCD_ROWS, dotsize=8, charmap='A02', auto_linebreaks=True)

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature, humidity, pressure):
    """
    Send sensor data to ThingSpeak
    """
    try:
         # Construct the payload
        payload = {
            'api_key': THINGSPEAK_API_KEY,
            'field1': temperature,
            'field2': humidity,
            'field3': pressure
        }
        
        # Send the HTTP POST request
        response = requests.post(THINGSPEAK_URL, data=payload)
        
        # Check the response
        if response.status_code == 200:
            print("Data successfully sent to ThingSpeak")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
        
        response.close()
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")

# Function to read sensor data
def read_sensor_data():
    temperature = bmp280.temperature
    pressure = bmp280.pressure
    altitude = bmp280.altitude
    humidity = dht_device.humidity
    
    return temperature, pressure, altitude, humidity

# Function to display data on LCD
def display_data(temperature, pressure, altitude, humidity):
    # Clear the display
    lcd.clear()
    
    # Format the temperature and pressure data
    temp_str = f"Temp: {temperature:.1f}C "
    pressure_str = f"Press: {pressure:.1f}hPa"
    
    # Display on LCD
    lcd.cursor_pos = (0, 0)  # First row
    lcd.write_string(temp_str)
    
    lcd.cursor_pos = (1, 0)  # Second row
    lcd.write_string(pressure_str)
    
    # Wait for a few seconds
    time.sleep(3)
    
    # Display altitude on the second screen
    lcd.clear()
    lcd.cursor_pos = (1, 0)  # Second row
    lcd.write_string(f"Altitude: {altitude:.1f} m")
    
    lcd.cursor_pos = (0, 0)  # First row
    lcd.write_string(f"Humidity: {humidity:.1f}%")
    
    # Wait before refreshing
    time.sleep(3)

# Main loop
try:
    print("Weather Station Running...")
    print("Press CTRL+C to exit")
    while True:
        
        # Read data from sensor
        temperature, pressure, altitude, humidity = read_sensor_data()
        
        # Print data to console for debugging
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Pressure: {pressure:.1f}hPa")
        print(f"Altitude: {altitude:.1f} meters")
        print(f"Humidity: {humidity:.1f}%")
        print("-" * 30)
        
        # Display data on LCD
        display_data(temperature, pressure, altitude, humidity)
        
        # Send data to ThingSpeak
        send_to_thingspeak(temperature, humidity, pressure)
        
        # Wait before the next reading
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Program stopped by user")
    lcd.clear()
    lcd.write_string("Weather Station")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Shutting down...")
    time.sleep(2)
    lcd.clear()
finally:
    # Clean up
    lcd.close(clear=True)
    print("Weather station shut down")
