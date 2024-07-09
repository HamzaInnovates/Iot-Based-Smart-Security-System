# servo_control.py

import time
from pyfirmata2 import Arduino, SERVO

ARDUINO_PORT = 'COM5'
SERVO_PIN = 9

board = Arduino(ARDUINO_PORT)
board.digital[SERVO_PIN].mode = SERVO

def control_servo(angle, delay=10):
    
    board.digital[SERVO_PIN].write(angle)
    time.sleep(delay)
# control_servo(40)    
    
    
