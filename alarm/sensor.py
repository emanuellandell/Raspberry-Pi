import Adafruit_DHT
import RPi.GPIO as GPIO
import json
import time

# Setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def read_and_send_data():
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if temperature is not None:
            data = {"temperature": temperature, "humidity": humidity}
            with open("/home/pi/sensor_data.json", "w") as file:
                json.dump(data, file)
            if temperature > 25:  # Ändra 25 till din tröskeltemperatur
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(5)

try:
    read_and_send_data()
except KeyboardInterrupt:
    GPIO.cleanup()
