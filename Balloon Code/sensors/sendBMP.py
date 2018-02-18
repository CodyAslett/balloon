#!/usr/bin/python
from Adafruit_BMP085 import BMP085
import serial
import time

bmp = BMP085(0x77) # Temp, pressure, altitude sensor

port = '/dev/ttyACM0'
ser = serial.Serial(port, 9600)

i = 0

while True:

   tempC = bmp.readTemperature()
   preshPa = (bmp.readPressure() / 100)
   altitudeM = bmp.readAltitude()
   i += i

   print tempC

# BMP085 Barometic Pressure Sensor # includes Temperature and Altitude


#send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("send ")
   ser.write("KF7VHP-1") 
   ser.write(" BMP:")
   ser.write("T:%dC" % int(tempC))
   ser.write("P:%dhPa" % int(preshPa))
   ser.write("A:%dm" % int(altitudeM))

   ser.write("\r\n")
   time.sleep(60)
