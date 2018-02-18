#!/bin/bash
DATE=$(date +"__%Y-%m-%d__%H:%M:%S")

COUNTER=0

  echo
  raspivid -o /home/pi/Pics/pyCamVideo/$COUNTER$DATE.h264 -t 10000 -vf -hf
  echo $COUNTER$DATE


