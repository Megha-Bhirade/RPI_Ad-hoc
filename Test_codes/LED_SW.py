# ---------------------------
# Basic GPIO Input & Output
# Pinout Mapping: https://pinout.xyz/pinout/pin3_gpio2
# ---------------------------

import RPi.GPIO as io
io.setmode(io.BOARD) # io.BCM for BCM format
io.setwarnings(False)

SW = 7 #GPIO 23
LED1 = 11 #GPIO 17
LED2 = 16 #GPIO 23
LED3 = 18 #GPIO 24
from time import sleep

#initialisation of LED pins
io.setup(LED1, io.OUT)
io.setup(LED2, io.OUT)
io.setup(LED3, io.OUT)

#initialisation of switch pin
io.setup(SW, io.IN)

while True:
    if io.input( SW ) == 0:
        io.output(LED1, 1) # 0 or 1 
        io.output(LED2, 0)
        io.output(LED3, 0)
        sleep(0.5)
        io.output(LED1, 0) # 0 or 1 
        io.output(LED2, 1)
        io.output(LED3, 0)
        sleep(0.5)
        io.output(LED1, 0) # 0 or 1 
        io.output(LED2, 0)
        io.output(LED3, 1)
        sleep(0.5)
     
    else:
        io.output(LED1, 0)
        io.output(LED2, 0)
        io.output(LED3, 0)
        



