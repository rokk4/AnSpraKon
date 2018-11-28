# AnSpraKon
Reads 7-Segment Displays with OpenCV and SSOCR, than speak the output with nanoTTS.

AnSpraKon is developed by [AG Koch -Semiconductor Photonics](https://www.uni-marburg.de/en/fb13/semiconductor-photonics) at [Philipps-Universität Marburg](https://www.uni-marburg.de).



AnSpraKon is thought to be used with SBC's.



The provided ArchARM image is an usable example for the RPi 1 Modell A+.

# Dependencies
* Python3
* OpenCV 3
* ssocr [Official ssocr Website](http://www.unix-ag.uni-kl.de/~auerswal/ssocr/) [Github Mirror](https://github.com/auerswal/ssocr)
* [nano-tts](https://github.com/gmn/nanotts)

# Usage
```
usage: ansprakon.py [-h] [-b] [-m] [-f] [-r] [-g GPIOPIN] [-c CAM]
                    [-s <0.2-5.0>] [-p <0.5-2.0>] [-v <0.0-5.0>]
                    [-l {en-US,en-GB,de-DE,es-ES,fr-FR,it-IT}]
                    [-q BUFFER [BUFFER ...]] [--version]
                    device

read 7-segment displays and read out the result

positional arguments:
  device                enter the ID of the device to use

optional arguments:
  -h, --help            show this help message and exit
  -b, --button          speak on button press
  -m, --mute            don't speak
  -f, --final           device which displays a final result
  -r, --rpi             run on rpi
  -g GPIOPIN, --gpiopin GPIOPIN
                        set the GPIO pin
  -c CAM, --cam CAM     set the device index of the cam to use
  -s <0.2-5.0>, --speed <0.2-5.0>
                        set speed of the voice
  -p <0.5-2.0>, --pitch <0.5-2.0>
                        set the pitch of the voice
  -v <0.0-5.0>, --volume <0.0-5.0>
                        set the volume of the voice
  -l {en-US,en-GB,de-DE,es-ES,fr-FR,it-IT}, --language {en-US,en-GB,de-DE,es-ES,fr-FR,it-IT}
                        set the language of the voice
  -q BUFFER [BUFFER ...], --buffer BUFFER [BUFFER ...]
                        min. bufferlength and min. result count to be the
                        finalresult
  --version             show program's version number and exit
```
