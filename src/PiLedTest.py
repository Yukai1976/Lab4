import socket
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):

    led.set_output(0, 1)
    time.sleep(delay)
    led.set_output(0, 0)
    time.sleep(delay)

def blink_led_5(delay):
    times = int(5/(delay*2))
    for i in range(times):
        led.set_output(0, 1)
        time.sleep(delay)
        led.set_output(0, 0)
        time.sleep(delay)
    led.set_output(0, 0)


def main():
    switch.init()
    led.init()
    if(switch.read_slide_switch() == 1):
        blink_led(0.1)
    else:
        blink_led_5(0.05)
        led.set_output(0, 0)



if __name__ == "__main__":
    main()
