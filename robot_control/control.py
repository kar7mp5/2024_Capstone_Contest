# control.py
import RPi.GPIO as GPIO
import time




class Controller:
    def __init__(self, bl_pin, fl_pin, br_pin, fr_pin):
        """Control the robot by raspberrypi5

        This code is based on the following site.
        https://sharad-rawat.medium.com/interfacing-l298n-h-bridge-motor-driver-with-raspberry-pi-7fd5cb3fa8e3

        Caution!
        It may not work if both the front and back pins are GPIO.HIGH.
        That is, either one of them must be GPIO.HIGH or both must be GPIO.LOW.

        Args:
            _bl_pin (int): back left pin;   if this pin is GPIO.HIGH, left motor would be to back.
            _fl_pin (int): front left pin;  if this pin is GPIO.HIGH, left motor would be to front.
            _br_pin (int): back right pin;  if this pin is GPIO.HIGH, right motor would be to back.
            _fr_pin (int): front right pin; if this pin is GPIO.HIGH, right motor would be to front.
        """
        # setup motor pins
        self._bl_pin = bl_pin
        self._fl_pin = fl_pin
        self._br_pin = br_pin
        self._fr_pin = fr_pin
        GPIO.setmode(GPIO.BCM) # set the pin style BCM
        GPIO.setwarnings(False) 

        self.reset_pin()


    def reset_pin(self):
        """Reset pin setting to OUT"""
        GPIO.setup(self._bl_pin, GPIO.OUT) # back left pin
        GPIO.setup(self._fl_pin, GPIO.OUT) # front left pin
        GPIO.setup(self._fr_pin, GPIO.OUT) # front right pin
        GPIO.setup(self._br_pin, GPIO.OUT) # back right pin        


    def forward(self):
        """Go forward
        
        Args:
            sec (int): moving time.
        """
        GPIO.output(self._bl_pin, GPIO.LOW)
        GPIO.output(self._fl_pin, GPIO.HIGH)
        GPIO.output(self._fr_pin, GPIO.HIGH)
        GPIO.output(self._br_pin, GPIO.LOW)
        
        
    def go_back(self):
        """Go back
        
        Args:
            sec (int): moving time.
        """
        GPIO.output(self._bl_pin, GPIO.HIGH)
        GPIO.output(self._fl_pin, GPIO.LOW)
        GPIO.output(self._fr_pin, GPIO.LOW)
        GPIO.output(self._br_pin, GPIO.HIGH)
        
        
    def left_turn(self):
        """Turn left
        
        Args:
            sec (int): moving time.
        """
        GPIO.output(self._bl_pin, GPIO.HIGH)
        GPIO.output(self._fl_pin, GPIO.LOW)
        GPIO.output(self._fr_pin, GPIO.HIGH)
        GPIO.output(self._br_pin, GPIO.LOW)
        

    def right_turn(self):
        """Turn right
        
        Args:
            sec (int): moving time.
        """
        GPIO.output(self._bl_pin, GPIO.LOW)
        GPIO.output(self._fl_pin, GPIO.HIGH)
        GPIO.output(self._fr_pin, GPIO.LOW)
        GPIO.output(self._br_pin, GPIO.HIGH)


    def stop(self):
        GPIO.cleanup()