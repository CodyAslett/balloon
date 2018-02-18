#!/usr/bin/evn python


# set to run at boot by adding it to bash script etc/rc.local


#********* Libraries *********#

import csv
import time
import datetime
import os
import sys
import picamera

sys.path.insert(0, '/path/to/application/app/folder') # so libraries below will work as it boots during boot up 

from Adafruit_BMP085 import BMP085
from TSL2561 import TSL2561
import Adafruit_DHT
from ADC import MCP3008ADC



#********* Global *********#

# values
saveLocation = "/home/pi/sensors/sensorData.csv"
timeZone     = "America/Denver" # this comes from List of tz database time zones

# Initialise Sensors
try:
  bmp = BMP085(0x77) # Temp, pressure, altitude sensor
except:
  print "BMP Sensor Fail"
# fixed text
csvTop = ["Count", "Date", "Time", "BMP Temp", "BMP Press", "BMP Alt ", "TSL High", "TSL Low ", "TSL Auto", "SI1 Vis ", "SI1 IR  ", "SI1 UV  ", "LSM  R  ", "LSM  P  ", "LSM  Y  ", "LSM  X  ", "LSM  Y  ", "LSM  Z  ", "AM2 Temp", "AM2 Humi", "MCP ACD1", "MCP ACD2", "MCP ACD3", "MCP ACD4", "MCP ACD5", "MCP ACD6", "MCP ACD7", "MCP ACD8"]
bootText = [datetime.datetime.now().strftime("starting sensor collection on %a %d of %b %Y  at  %I:%M:%S %p  %Z%z")]

# Data Values
count    = 0
date     = datetime.datetime.now().strftime("%d/%m/%Y")
HMS      = datetime.datetime.now().strftime("%I:%M:%S %p")
bmpTemp  = -2
bmpPress = -2
bmpAlt   = -2
tslHigh  = -2
tslLow   = -2
tslAuto  = -2
si1Vis   = -2
si1Ir    = -2
si1Uv    = -2
lsmR     = -2
lsmP     = -2
lsmy     = -2
lsmX     = -2
lsmY     = -2
lsmZ     = -2
am2Temp  = -2
am2Humi  = -2
acd1     = -2
acd2     = -2
acd3     = -2
acd4     = -2
acd5     = -2
acd6     = -2
acd7     = -2
acd8     = -2





#********* Functions *********#

###########################################################
# Statup 
# the one time setup functions and actions 
#
###########################################################
def startup():
    # Set time Zone
    os.environ['TZ'] = timeZone
    
    print bootText
    
    csv_out = open(saveLocation, 'a') # the 'a' is for apending
    mywriter = csv.writer(csv_out)
    mywriter.writerow(bootText)
    mywriter.writerow(csvTop)
    csv_out.close()

    return



###########################################################
# Fill Data 
# the one time setup functions and actions 
#
###########################################################
def fillData():
# Date and Time
  os.environ['TZ'] = timeZone
  date       = datetime.datetime.now().strftime("%d/%m/%Y")
  HMS        = datetime.datetime.now().strftime("%I:%M:%S %p")

# BMP085 - Temperature, Barometic Pressure, Altitude
  try:
    bmpTemp  = bmp.readTemperature()
  except:
    bmpTemp = -1
  try:
    bmpPress = (bmp.readPressure() / 100.0)
  except:
    bmpPress = -1
  try:
    bmpAlt   = bmp.readAltitude()
  except:
    bmpAlt = -1

# TSL2561 - Lux Sensor
  try:
    tslHigh = tsl.readLux(16)
  except:
    tslHigh = -1
  try:
    tslLow = tsl.readLux(1)
  except:
    tslLow = -1
  try: 
    tslAuto = tsl.readLux()
  except:
    tslAuto = -1
    
# AM2302 - Temperatrue, Humidity
  try:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 27) # Yellow wire on PIN 27
    am2Temp = temperature
    am2Humi = humidity
  except:
    am2Temp = -1
    am2Humi = -1
    
# MCP3008 - analog to digital converter
  try:
    acd1 = MCP3008ADC(0)
  except:
    acd1 = -1
  try:
    acd2 = MCP3008ADC(1)
  except:
    acd2 = -1
  try:
    acd3 = MCP3008ADC(2)
  except:
    acd3 = -1
  try:
    acd4 = MCP3008ADC(3)
  except:
    acd4 = -1
  try:
    acd5 = MCP3008ADC(4)
  except:
    acd5 = -1
  try:
    acd6 = MCP3008ADC(5)
  except:
    acd6 = -1
  try:
    acd7 = MCP3008ADC(6)
  except:
    acd7 = -1
  try:
    acd8 = MCP3008ADC(7)
  except:
    acd8 = -1
  
    

  outToFile = [count, date, HMS, bmpTemp, bmpPress, bmpAlt, tslHigh, tslLow, tslAuto, si1Vis, si1Uv, lsmR, lsmP, lsmy, lsmX, lsmY, lsmZ, am2Temp, am2Humi, acd1, acd2, acd3, acd4, acd5, acd6, acd7, acd8]
  print outToFile
  
  csv_out = open(saveLocation, 'a')
  mywriter = csv.writer(csv_out)
  mywriter.writerow(outToFile)
  csv_out.close()
  

  return





###########################################################
# main program start
# 
#
###########################################################
startup()
while True:
  fillData()
  print
  print
  print
  print count
  time.sleep(5)
  count = count + 1
  
