#!/bin/bash
# sstv camera, Gerrit Polder, PA3BYA
# shell script to test SSTV camera
raspistill -t 1 --width 320 --height 256 -e png -o /tmp/image.png
# add callsign
mogrify -pointsize 24 -draw "text 10,40 'KG7PAG'" /tmp/image.png
./pisstv /tmp/image.png 22050
sudo ./pifm_sstv /tmp/image.png.wav
rm /tmp/image.png*