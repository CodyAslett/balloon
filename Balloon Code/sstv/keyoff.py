import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)
print "Key off radio"
GPIO.output(25,GPIO.LOW)
