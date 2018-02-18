#numLoops=10
#loopCount=0

#while [ $loopCount -lt $numLoops ]
#do
	#echo $loopCount of $numLoops

	#TAKE PIC
	echo TAKE PICTURE
	raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
	#ADD CALL SIGN
	echo ADD CALL SIGN
	mogrify -pointsize 24 -fill blue -draw "text 10,40 'KG7PAG'" imagetest.png
	#GENERATE WAV
	echo GENERATE AUDIO
	sudo ./pisstv imagetest.png 22050
	echo SEND PICTURE
	sudo python keyon.py
	#PLAY WAV
	aplay imagetest.png.wav
	sudo python keyoff.py

#	loopCount='expr $loopCount +1'
#done



#SEND PIC
#sudo ./pifm imagetest.png.wav

