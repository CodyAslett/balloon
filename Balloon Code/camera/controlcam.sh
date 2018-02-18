#!/bin/bash
DATE=$(date +"__%Y-%m-%d__%H:%M:%S")

COUNTER=0


  echo
  raspistill -vf -hf -o /home/pi/Pics/pyCam/$COUNTER$DATE.jpg
  echo $COUNTER$DATE
  echo
  fswebcam -r 1920x1080 --no-banner /home/pi/Pics/webCam/$COUNTER$DATE.jpg
  echo
 

