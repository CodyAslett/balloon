#!/usr/bin/python
import Adafruit_DHT
import serial
import time


while True:
   print ""

   print "AM2302 - Temperatrue, Humidity"
   print "------------------------------------------------------------"
   humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   print "temperatrue %f" % temperatureC 
   print "humidity  : %f" % humidity 

   print ""
   print ""
   print ""


   print "Welcome to send APRS DHT"

   port = '/dev/ttyACM0'
   ser = serial.Serial(port, 9600)

   #send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("send ")
   ser.write("KF7VHP-1") 
   ser.write(" DHT:")
   ser.write("T:%dC" % int(temperatureC))
   ser.write("H:%dPH" % int(humidity))
   ser.write("\r\n")
   #time.sleep(180)
