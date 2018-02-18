import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math


SETTINGS_FILE = "RTIMULib"
s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

x, y, z = imu.getFusionData()


def LSM9DS0R():
  if (not imu.IMUInit()):
    print("IMU Init Failed");

  poll_interval = imu.IMUGetPollInterval()

  if imu.IMURead():
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
    time.sleep(poll_interval*1.0/1000.0)
    
  return(math.degrees(fusionPose[0]))






def LSM9DS0P():
  if (not imu.IMUInit()):
    print("IMU Init Failed");

  poll_interval = imu.IMUGetPollInterval()

  if imu.IMURead():
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
    
  return(math.degrees(fusionPose[1]))





def LSM9DS0Y():
  if (not imu.IMUInit()):
    print("IMU Init Failed");

  poll_interval = imu.IMUGetPollInterval()
  if imu.IMURead():
    data = imu.getIMUData()
    fusionPose = data["fusionPose"]
    
  return(math.degrees(fusionPose[2]))





def LSM9DS0X(): 
  return x





def LSM9DS0AY(): 
  return y
  




def LSM9DS0Z(): 
  return z