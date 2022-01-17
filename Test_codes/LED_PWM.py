# ---------------------------------
# Basic PWM functionality in Raspberry Pi
# --------------------------------

import RPi.GPIO as io
io.setmode(io.BOARD) # io.BCM for BCM format
io.setwarnings(False)

pwm_fw= 100
brakeInterval = -2

pwm_pin_R = 32
pwm_pin_G = 33
GPIO_pin_B = 37
SW = 38 #GPIO 20

from time import sleep

#initialisation of LED pins
io.setup(GPIO_pin_B, io.OUT)

#initialisation of PWM channels
io.setup( pwm_pin_R, io.OUT )
io.output( pwm_pin_R, 0 )

io.setup( pwm_pin_G, io.OUT )
io.output( pwm_pin_G, 0 )

#initialisation of switch pin
io.setup(SW, io.IN)

pwmObjR = io.PWM( pwm_pin_R, 1000 )  # frequency =1000
pwmObjG = io.PWM( pwm_pin_G, 1000 )  # frequency =1000


pwmObjR.start(0) # starting duty cycle
pwmObjG.start(0) # starting duty cycle


while True:
    if io.input( SW ) == 0:
        for dc in range( pwm_fw, -1 , brakeInterval ):
            pwmObjR.ChangeDutyCycle( dc )
            pwmObjG.ChangeDutyCycle( 100-dc )
            sleep(.1)
        io.output(GPIO_pin_B, not io.input( GPIO_pin_B ))
        #sleep(.5)
        #io.output(GPIO_pin_B, 0)
        
