import RPi.GPIO as GPIO
import dht11
import time
import datetime
import commands

SLEEP_SEC = 1800

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
# instance = dht11.DHT11(pin=14)
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    #print result
    
    if result.is_valid():
        #print("Last valid input: " + str(datetime.datetime.now()))
        #print("Temperature: %d C" % result.temperature)
        #print("Humidity: %d %%" % result.humidity)

        # Get Temperature and Humidity
        temperature = result.temperature
        humidity = result.humidity

        # Throw data to Focuslight
        output = commands.getoutput("curl -F number=" + str(temperature) + " http://localhost:8888/api/home/sensor/temperature")
        output = commands.getoutput("curl -F number=" + str(humidity) + " http://localhost:8888/api/home/sensor/humidity")

    time.sleep(SLEEP_SEC)
