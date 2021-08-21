#toggle_LED_system.py
#gpio2 is red led
#gpio3 is green led
#gpio4 is white led
#gpio14 is button

from signal import pause
from gpiozero import LED, Button
from time import sleep

button = Button(14)

rled = LED(2)
gled = LED(3)
wled = LED(4)

inOut = True
inside = False
outside = True


def inOutCycle():

    global inOut

    if inOut:
        rled.off()
        gled.on()
        wled.on()
        sleep(5)
        
        inOut = False
        
    else:
        rled.on()
        gled.off()
        wled.off()
        sleep(5)
        
        inOut = True
                    
try:

    button.when_pressed = inOutCycle
    pause()

finally:
    pass
