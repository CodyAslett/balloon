#!/bin/bash




# update pi
sudo apt-get update -y
sudo apt-get upgrade -y



# GPIO
sudo apt-get install python-dev -y
sudo apt-get install python-setuptools -y
sudo apt-get install build-essential python-dev -y
sudo apt-get install python-rpi.gpio -y



# I2C
sudo apt-get install python-smbus -y
sudo apt-get install i2c-tools -y



#ADC
#      ---U---
# CH0 |   M   | VDD 
# CH1 |   C   | V REF
# CH2 |   P   | A GND
# CH3 |   3   | CLK
# CH4 |   0   | D OUT
# CH5 |   0   | D IN
# CH6 |   8   | CS/SHDN
# CH7 |       | D GND
#      -------

sudo easy_install rpi.gip -y

sudo apt-get install alsa-utils -y
sudo apt-get install mpg321 -y



# BMP
sudo python /install/Adafruit_Python_BMP/ setup.py install

cd install/Adafruit_Python_BMP
sudo python setup.py install
cd ../..



# DHT
cd install/Adafruit_Python_DHT
sudo python setup.py install
cd ../..



# ?Gyro?
cd install/RTIMULib-master/RTIMULib-master/Linux/python
sudo python setup.py install
cd ../../../../..

echo
echo
echo
echo
echo

#run test 
sudo python displaySensors.py