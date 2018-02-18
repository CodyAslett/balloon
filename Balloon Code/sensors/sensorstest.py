#!/usr/bin/python
from Adafruit_BMP085 import BMP085
import Adafruit_DHT
import serial
import time

fileOut = open('sensorOut1.csv','a+')

fileOut.write("test")

bmp = BMP085(0x77) # Temp, pressure, altitude sensor
DHTPIN = 17
i = 0

while True:

   tempC = bmp.readTemperature()
   preshPa = (bmp.readPressure() / 100)
   altitudeM = bmp.readAltitude()
   i += i
   
   print "-------------------------------------------------------------"
   print "BMP DATA:\n"
   print "Temperatrue  : %f C" % tempC

   print "Pressure  : %f hPa" % preshPa

   print "Altitude  : %f m" % altitudeM



   print "\n\nAM2302 Data:\n"

   humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   print "Temperatrue : %f C" % temperatureC
  
   print "humidity  : %f P" % humidity 

   print "-------------------------------------------------------------"

 



humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, DHTPIN) # Yellow
