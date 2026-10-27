import time
import board
import adafruit_dht

# Initialize the DHT11 sensor on GPIO 4 (Pin 7)
# Change board.D4 to match your data pin if you chose a different one
dht_device = adafruit_dht.DHT11(board.D4)

print("Starting DHT11 sensor readings... Press Ctrl+C to exit.\n")

while True:
    try:
        # Read temperature and humidity values
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        
        # Convert Celsius to Fahrenheit
        temperature_f = temperature_c * (9 / 5) + 32

        # Format and display the output
        print(f"Temp: {temperature_c:.1f}C ({temperature_f:.1f}F) | Humidity: {humidity:.1f}%")

    except RuntimeError as error:
        # DHT sensors can be temperamental and drop readings frequently.
        # This prevents the script from crashing when a single reading fails.
        print(f"Reading missed: {error.args[0]}")
        time.sleep(2.0)
        continue
        
    except Exception as error:
        dht_device.exit()
        raise error

    # The DHT11 requires a minimum 2-second delay between successful readings
    time.sleep(2.0)