import RPi.GPIO as gpio
import time


def gpio_callback():
    print("Button Pushed")


gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(11, gpio.RISING, callback=gpio_callback())

while True:
    time.sleep(4)
    print("Not Pushed")
