import Adafruit_DHT as dht
from time import sleep
#Set DATA pin
DHT = 2 #Put GPIO Pin Number
while True:
    #Read Temp and Hum from DHT22
    h,t = dht.read(dht.DHT22, DHT)
    #Print Temperature and Humidity on Shell window
    print('Temperature={0:0.1f}0 C  Humidity={1:0.1f}0 %'.format(t,h))
    sleep(2) #Wait 5 seconds and read again
