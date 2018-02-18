#!/bin/bash
DATE=$(date +"%Y-%m-%d__%H_%M_%S")
COUNTER=0

while true;
do
  echo
  raspistill -vf -hf -o /home/pi/Pics/pyCam/$COUNTER$DATE.jpg
  echo
  fswebcam -r 1920x1080 --no-banner /home/pi/Pics/webCam/$COUNTER$DATE.jpg
  echo
  let COUNTER=COUNTER+1
  echo 
  sleep 5
done