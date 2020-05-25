import RPi.GPIO as GPIO
import dht11
import time
import datetime
class DHTSensor(object):
	
	def __init__(self, channel):
		self.channel = channel 

	def __provision(self):

		GPIO.setmode(GPIO.BCM)
		
		time.sleep(1)
		
		GPIO.setup(self.channel, GPIO.OUT)
		GPIO.output(self.channel, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(self.channel, GPIO.HIGH)
		GPIO.setup(self.channel, GPIO.IN)
		
		while GPIO.input(self.channel) == GPIO.LOW:
			continue
		while GPIO.input(self.channel) == GPIO.HIGH:
			continue
		GPIO.cleanup()
		time.sleep(2)

	def get_number(self):
		self.__provision()
		GPIO.setwarnings(True)
		GPIO.setmode(GPIO.BCM)

		instance = dht11.DHT11(pin=4)


		result = instance.read()
		return result.temperature, result.humidity, str(datetime.datetime.now())


if __name__ == "__main__":
	sensor = DHTSensor(4)
	print(sensor.get_number())
