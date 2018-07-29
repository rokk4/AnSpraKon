import RPi.GPIO as gpio
import time


def gpio_callback(channel):
    print("Button Pushed")


gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.add_event_detect(11, gpio.FALLING, callback=gpio_callback, bouncetime=200)

while True:
    time.sleep(4)
    print("Not Pushed")
