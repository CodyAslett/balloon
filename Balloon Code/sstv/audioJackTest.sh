#!/bin/bash

#numLoops=10
#loopCount=0

#while true; DO ONCE - CODY M
#do
	#echo $loopCount of $numLoops

	#TAKE PIC
	echo TAKE PICTURE
	raspistill -t 1 --width 320 --height 256 -e png -o /home/pi/sstv/imagetest.png
	#ADD CALL SIGN
	echo ADD CALL SIGN
	mogrify -pointsize 24 -fill blue -draw "text 10,40 'K7BYI'" /home/pi/sstv/imagetest.png
	#GENERATE WAV
	echo GENERATE AUDIO
	sudo /home/pi/sstv/./pisstv /home/pi/sstv/imagetest.png 22050
	echo SEND PICTURE
	sudo python /home/pi/sstv/keyon.py
	#PLAY WAV
	aplay /home/pi/sstv/imagetest.png.wav
	sudo python /home/pi/sstv/keyoff.py

  #sleep 8m
#	loopCount='expr $loopCount +1'
#done



#SEND PIC
#sudo ./pifm imagetest.png.wav

