from Adafruit_BMP085 import BMP085
from TSL2561 import TSL2561
from ADC import MCP3008ADC
import SI1145 as SI1145
import Adafruit_DHT


from Fusion import LSM9DS0R, LSM9DS0P, LSM9DS0Y, LSM9DS0X, LSM9DS0AY, LSM9DS0Z


# Initialise Sensors
bmp = BMP085(0x77) # Temp, pressure, altitude sensor
  # we may want bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
tsl = TSL2561() # Lux sensor
#sensor = SI1145.SI1145() #



print ""

# BMP085 Barometic Pressure Sensor # includes Temperature and Altitude
print "BMP085 - Temperature, Barometic Pressure, Altitude"
print "-------------------------------------------------------------"
print "Temperature:%f  C " % bmp.readTemperature()
print "Pressure:   %f hPa" % (bmp.readPressure() / 100.0)
print "Altitude:   %f m  " % bmp.readAltitude()

print ""
print ""
print ""

# TSL2561 Lux Sensor # No idea what this is

print "TSL2561 - Lux Sensor"
print "-------------------------------------------------------------"
print "LUX HIGH GAIN ", tsl.readLux(16)
print "LUX LOW GAIN  ", tsl.readLux(1)
print "LUX AUTO GAIN ", tsl.readLux()

print ""
print ""
print ""

# SI1145 UV Sensor # 

print "SI1145 - Light Sensor"
print "-------------------------------------------------------------"
#print "Visible:    %s" % str(sensor.readVisible())
#print "IR:         %s" % str(sensor.readIR())
#print "UV Index:   %s" % str(sensor.readUV())

print ""
print ""
print ""

#FLORA 9-DOF/ LSM9DS0 accelerometer-gyro-magnetometer # I don't know if this is working right # requries intall
print "FLORA 9-DOF/ LSM9DS0 - accelerometer, gyro, magnetometer"
print "-------------------------------------------------------------"
#print "gyro raw R: %f" % LSM9DS0R()
#print "gyro raw P: %f" % LSM9DS0P()
#print "gyro raw Y: %f" % LSM9DS0Y()
#print "         X: %f" % LSM9DS0X()
#print "         Y: %f" % LSM9DS0AY()
#print "         Z: %f" % LSM9DS0Z()

print ""
print ""
print ""

print "AM2302 - Temperatrue, Humidity"
print "-------------------------------------------------------------"
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 27) # Yellow wire on PIN 27
print "temperatrue %f" % temperature 
print "humidity  : %f" % humidity 

print ""
print ""
print ""

print "MCP3008 - analog to digital converter"
print "-------------------------------------------------------------"
print "ADC 1: %i" % MCP3008ADC(0)
print "ADC 2: %i" % MCP3008ADC(1)
print "ADC 3: %i" % MCP3008ADC(2)
print "ADC 4: %i" % MCP3008ADC(3)
print "ADC 5: %i" % MCP3008ADC(4)
print "ADC 6: %i" % MCP3008ADC(5)
print "ADC 7: %i" % MCP3008ADC(6)
print "ADC 8: %i" % MCP3008ADC(7)

print ""