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

  
   tempF = 1.8*tempC + 32
   altitudeF = altitudeM*3.28084

#send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("send ")
   ser.write("KF7VHP-1") 
   ser.write(" BMP:")
   ser.write("T:%dF" % int(tempF))
   ser.write("P:%dhPa" % int(preshPa))
   ser.write("A:%df" % int(altitudeF))

   ser.write("\r\n")
   time.sleep(3)


#***********FUNCTION SEND DHT************
def sendDHT(temperatureC,humidity):

   print "SEND DHT"

   port = '/dev/ttyACM0'
   ser = serial.Serial(port, 9600)

   temperatureF = 1.8*temperatureC + 32

   #send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("send ")
   ser.write("KF7VHP-1") 
   ser.write(" DHT:")
   ser.write("T:%dF" % int(temperatureF))
   ser.write("H:%dPH" % int(humidity))
   ser.write("\r\n")
   time.sleep(3)


#***********FUNCTION SEND STATUS************
def sendSTATUS(A,B):

   print "SEND STATUS"

   port = '/dev/ttyACM0'
   ser = serial.Serial(port, 9600)

   #send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("send ")
   ser.write("KF7VHP-1") 
   ser.write(" STATUS:")
   ser.write(A)
   ser.write(B)
   ser.write("\r\n")
   time.sleep(3)


#***********FUNCTION SEND STATUS************
def sendBeacon():

   print "SEND APRS BEACON"

   port = '/dev/ttyACM0'
   ser = serial.Serial(port, 9600)

   #send commands
   ser.write("\r\n")

   ser.write("\r\n")
   ser.write("BEACON ")
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
blackBox = open('blackBoxLog1.csv', 'a+')

fileOut.write("\n")
fileOut.write("DATE(UTC), TIME(UTC), BMPTEMP(C), BMPP(hPa), BMPALT(M), DHTT(C), DHTH(%),\n")

blackBox.write("\n")
blackBox.write("DATE(UTC), TIME(UTC), COMMAND,\n")

bmp = BMP085(0x77) # Temp, pressure, altitude sensor
DHTPIN = 17
count = 1

tempC = 0
preshPa = 0
altitudeM = 0
temperatureC = 0
humidity = 0

while True:


   try:
      print "Count: %i \n" % count
      print "\n"
      tempC = bmp.readTemperature()
      preshPa = (bmp.readPressure() / 100)
      altitudeM = bmp.readAltitude()
   
   finally:
      print ""        
   
   #tempC = bmp.readTemperature()
   #preshPa = (bmp.readPressure() / 100)
   #altitudeM = bmp.readAltitude()

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
   
   try:
      humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   finally:
      print ""

   #humidity, temperatureC = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17) # Yellow wire on PIN 27

   print "Temperatrue : %f C" % temperatureC
   fileOut.write(str(temperatureC) + ",")
   print "humidity  : %f P" % humidity 
   fileOut.write(str(humidity) + ",")
   print "-------------------------------------------------------------"
   fileOut.write("\n")
#   sendBMP(tempC,preshPa,altitudeM)
 #  sendDHT(temperatureC,humidity)


   time.sleep(5) #Wait x seconds

   count = count + 1 #Iterator

   if count % 2 == 0:
      print("Take Pictures")
      subprocess.call("/home/pi/camera/./controlcam.sh") #Call the Picture PI CAM

      #Log in Black Box Record      
      blackBox.write(time.strftime("%d/%m/%Y"))
      blackBox.write(",")
      blackBox.write(time.strftime("%d:%M:%S"))
      blackBox.write(",")
      blackBox.write(" Took Pictures,\n")


   if count % 15 == 0: #TAKE 10 Second Video
      print("Take Video")
      subprocess.call("/home/pi/camera/./controlVideo.sh") #Call the Video
      
      #Log in Black Box Record
      blackBox.write(time.strftime("%d/%m/%Y"))
      blackBox.write(",")
      blackBox.write(time.strftime("%H:%M:%S"))
      blackBox.write(",")
      blackBox.write(" Took Video,\n")

	
   if count % 10  == 0:
      print("Send Data")
      sendBMP(tempC,preshPa,altitudeM)
      time.sleep(2) #Extra wait time
      sendDHT(temperatureC,humidity)

      #Log in Black Box Record
      blackBox.write(time.strftime("%d/%m/%Y"))
      blackBox.write(",")
      blackBox.write(time.strftime("%H:%M:%S"))
      blackBox.write(",")
      blackBox.write(" SENT BMP/DHT,\n")
      

   if count % 15 == 0:
      print("Send Beacon")
      sendBeacon()

      #Log in Black Box Record
      blackBox.write(time.strftime("%d/%m/%Y"))
      blackBox.write(",")
      blackBox.write(time.strftime("%H:%M:%S"))
      blackBox.write(",")
      blackBox.write(" SENT BEACON,\n")

   #if count % 45 == 0:
   #   print("Send SSTV")
   #   sendSTATUS(" SSTV", " SEND")
   #   subprocess.call("/home/pi/sstv/./controlsstv.sh") #Call the Picture PI CAM SEND

      #Log in Black Box Record
   #   blackBox.write(time.strftime("%d/%m/%Y"))
   #   blackBox.write(",")
   #   blackBox.write(time.strftime("%H:%M:%S"))
   #   blackBox.write(",")
   #   blackBox.write(" SENT SSTV,\n")
      





