#!/usr/bin/python
from Adafruit_BMP085 import BMP085
import Adafruit_DHT
import serial

bmp = BMP085(0x77) # Temp, pressure, altitude sensor


port = '/dev/ttyACM0'
ser = serial.Serial(port, 9600)

print ""

tempC = bmp.readTemperature()
preshPa = (bmp.readPressure() / 100)
altitudeM = bmp.readAltitude()

# BMP085 Barometic Pressure Sensor # includes Temperature and Altitude
print "BMP085 - Temperature, Barometic Pressure, Altitude"
print "-------------------------------------------------------------"
print "Temperature:%f  C " % tempC
print "Pressure:   %f hPa" % preshPa
print "Altitude:   %f m  " % altitudeM

print ""
print ""
print ""


print "SENDING"


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

print ""

print "AM2302 - Temperatrue, Humidity"
print "-------------------------------------------------------------"
humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 27) # Yellow wire on PIN 27

print "temperatrue %f" % temperatureC 
print "humidity  : %f" % humidity 

print ""
print ""
print ""

#send commands
ser.write("\r\n")

ser.write("\r\n")
ser.write("send ")
ser.write("KF7VHP-1") 
ser.write(" DHT:")
ser.write("T:%dC" % int(temperatureC))
ser.write("H:%dPH" % int(humidity))


ser.write("\r\n")