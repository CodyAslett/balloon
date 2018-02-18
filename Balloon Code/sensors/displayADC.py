from Adafruit_BMP085 import BMP085
from TSL2561 import TSL2561
from ADC import MCP3008ADC
import SI1145 as SI1145
import Adafruit_DHT


from Fusion import LSM9DS0R, LSM9DS0P, LSM9DS0Y, LSM9DS0X, LSM9DS0AY, LSM9DS0Z






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