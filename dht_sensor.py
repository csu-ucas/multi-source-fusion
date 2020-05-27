import RPi.GPIO as GPIO
import dht11
import time
import datetime
import socket
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
		print("provison finished")

	def get_number(self):
		self.__provision()
		GPIO.setwarnings(True)
		GPIO.setmode(GPIO.BCM)

		instance = dht11.DHT11(pin=4)


		result = instance.read()
		return result.temperature, result.humidity, str(datetime.datetime.now())


if __name__ == "__main__":
	sensor = DHTSensor(4)
	while True:
		data = sensor.get_number()
		if data[0] == 0 and data[1] == 0:
			pass
		else:
			string = str(("DTH", data[2], data[0], data[1]))
			print(string)
			print("%s: Temperature:%.1f, Humidity:%.1f"%(data[2], data[0], data[1]))
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('localhost', 60000))
			s.sendall(string.encode())
			# data = s.recv(1024)
			s.close()
		time.sleep(9)
	#print(sensor.get_number())
