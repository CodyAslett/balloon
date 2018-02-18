#!/usr/bin/python
from Adafruit_BMP085 import BMP085
from TSL2561 import TSL2561
import Adafruit_DHT
import serial
import time
import subprocess

sendToCall = "KF7VHP-1"

#***************FUNCTION DES***********
def sendBMP(tempC,preshPa,altitudeM):
   bmp = BMP085(0x77) # Temp, pressure, altitude sensor
   port = '/dev/ttyACM0'
   ser = serial.Serial(port, 9600)

   print "SENDING BMP\n"

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
   time.sleep(3)


#***********FUNCTION SEND DHT************
def sendDHT(temperatureC,humidity):

   print "SEND DHT"

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
   time.sleep(3)



#********* Global *********#

# values
saveLocation = "/home/pi/sensors/sensorOut1.csv"
timeZone     = "America/Denver" # this comes from List of tz database time zones

sendBMPMod = 10
sendDHTMod = 10
takePiCamMod = 100
takeWebCamMod = 100
sendPiCamMod = 100

fileOut = open('sensorOut1.csv','a+')

fileOut.write("\n")
fileOut.write("DATE, TIME, BMPTEMP(C), BMPP(hPa), BMPALT(M), DHTT(C), DHTH(%),\n")

bmp = BMP085(0x77) # Temp, pressure, altitude sensor
DHTPIN = 17
i = 0
count = 1

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


   print "\n\nAM2302 DATA:\n"

   humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   print "Temperatrue : %f C" % temperatureC
   fileOut.write(str(temperatureC) + ",")
   print "humidity  : %f P" % humidity 
   fileOut.write(str(humidity) + ",")
   print "-------------------------------------------------------------"
   fileOut.write("\n")



   time.sleep(5) #Wait x seconds

   count = count + 1 #Iterator

   if count % 2 == 0:
      subprocess.call("/home/pi/camera/./cambashcody.sh") #Call the Picture PI CAM SEND


   if count % 10 == 0:
      sendBMP(tempC,preshPa,altitudeM)
      sendDHT(temperatureC,humidity)
      
      

   if count % 40 == 0:
      subprocess.call("/home/pi/sstv/./audioJackTest.sh") #Call the Picture PI CAM SEND






