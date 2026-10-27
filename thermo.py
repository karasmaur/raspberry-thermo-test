import time
import Adafruit_DHT
import RPi.GPIO as gpio

pin = 15

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.IN)

sensor = Adafruit_DHT.DHT11

try:
    while True:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
            
        if hum is not None and temp is not None:
            print(temp)
            print(hum)
            time.sleep(1)
        else:
            print("veio vazio, algum erro")
except KeyboardInterrupt:
    print("---STOP----")
    gpio.cleanup()
    pass