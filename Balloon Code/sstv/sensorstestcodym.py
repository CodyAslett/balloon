#!/usr/bin/python
from Adafruit_BMP085 import BMP085
import Adafruit_DHT
import serial
import time
import subprocess

fileOut = open('sensorOut1.csv','a+')

fileOut.write("DATE, TIME, BMPTEMP(C), BMPP(hPa), BMPALT(M), DHTT(C), DHTH(%),\n")

bmp = BMP085(0x77) # Temp, pressure, altitude sensor
DHTPIN = 17
i = 0
count = 0

while True:

   tempC = bmp.readTemperature()
   preshPa = (bmp.readPressure() / 100)
   altitudeM = bmp.readAltitude()
   i += i
   
   fileOut.write(time.strftime("%d/%m/%Y"))
   fileOut.write(",")
   fileOut.write(time.strftime("%H:%M:%S"))
   fileOut.write(",")
   print "-------------------------------------------------------------"
   print "BMP DATA:\n"
   print "Temperatrue  : %f C" % tempC
   fileOut.write(str(tempC) + ",")
   print "Pressure  : %f hPa" % preshPa
   fileOut.write(str(preshPa) + ",")
   print "Altitude  : %f m" % altitudeM
   fileOut.write(str(altitudeM) + ",")


   print "\n\nAM2302 Data:\n"

   humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   print "Temperatrue : %f C" % temperatureC
   fileOut.write(str(temperatureC) + ",")
   print "humidity  : %f P" % humidity 
   fileOut.write(str(humidity) + ",")
   print "-------------------------------------------------------------"
   fileOut.write("\n")

   time.sleep(10)

   if count % 3 == 0:
      subprocess.call("./test.sh")


humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, DHTPIN) # Yellow
