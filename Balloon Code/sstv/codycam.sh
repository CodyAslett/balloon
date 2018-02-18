
#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST1'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav



#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST2'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav



#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST3'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav



#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST4'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav



#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST5'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav



#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST6'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav

#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST7'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav

#TAKE PIC
echo TAKE PICTURE
raspistill -t 1 --width 320 --height 256 -e png -o imagetest.png
#ADD CALL SIGN
echo ADD CALL SIGN
mogrify -pointsize 24 -fill blue -draw "text 10,40 'KF7VHP-TEST8'" imagetest.png
#GENERATE WAV
echo GENERATE AUDIO
sudo ./pisstv imagetest.png 22050
echo SEND PICTURE
#SEND PIC
sudo ./pifm imagetest.png.wav
