# ---------------------------
# Basic GPIO Input & Output
# Pinout Mapping: https://pinout.xyz/pinout/pin3_gpio2
# ---------------------------

import RPi.GPIO as io
io.setmode(io.BOARD) # io.BCM for BCM format
io.setwarnings(False)

SW = 16 #GPIO 23
LED= 11 #GPIO 17

io.setup(SW, io.IN)

#if io.input( SW ) == 1:
from time import sleep
io.setup(LED, io.OUT)
while True:
    io.output(LED, 1) # 0 or 1 
    sleep(1)
    io.output(LED, 0)
    sleep(1)


