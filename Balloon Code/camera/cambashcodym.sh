#!/bin/bash
DATE=$(date +"__%Y-%m-%d__%H:%M:%S")

COUNTER=38

while true;
do
  echo Capturing on Pi Cam
  raspistill -vf -hf -o /home/pi/Pics/pyCam/$COUNTER$DATE.jpg
  echo $COUNTER$DATE
  echo
  fswebcam -r 1920x1080 --no-banner /home/pi/Pics/webCam/$COUNTER$DATE.jpg
  echo

  echo 
  sleep 5
   


   if [[ $(( $COUNTER % 40 )) == 0 ]]; #REPLACE WITH MOD NUMBER TO PROVIDE OUR DELAY BASED ON SLEEP INTERVAL
   then 
      echo "IF THEN TRANSMIT"
      /home/pi/sstv/audioJackTest.sh 

   else
      echo "IF ELSE"
   fi

     let COUNTER=COUNTER+1

done
   
