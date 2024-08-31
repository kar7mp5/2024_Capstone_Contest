# control.py
import RPi.GPIO as gpio
import time




class Controller:
    def __init__(self, bl_pin, fl_pin, br_pin, fr_pin):
        """Control the robot by raspberrypi5

        This code is based on the following site.
        https://sharad-rawat.medium.com/interfacing-l298n-h-bridge-motor-driver-with-raspberry-pi-7fd5cb3fa8e3

        Caution!
        It may not work if both the front and back pins are TRUE.
        That is, either one of them must be True or both must be False.

        Args:
            _bl_pin (int): back left pin;   if this pin is true, left motor would be to back.
            _fl_pin (int): front left pin;  if this pin is true, left motor would be to front.
            _br_pin (int): back right pin;  if this pin is true, right motor would be to back.
            _fr_pin (int): front right pin; if this pin is true, right motor would be to front.
        """
        # setup motor pins
        self._bl_pin = bl_pin
        self._fl_pin = fl_pin
        self._br_pin = br_pin
        self._fr_pin = fr_pin

        self.reset_pin()


    def reset_pin(self):
        """Reset pin setting to OUT"""
        gpio.setmode(gpio.BCM) # set the pin style BCM
        gpio.setup(self._bl_pin, gpio.OUT) # back left pin
        gpio.setup(self._fl_pin, gpio.OUT) # front left pin
        gpio.setup(self._fr_pin, gpio.OUT) # front right pin
        gpio.setup(self._br_pin, gpio.OUT) # back right pin
        gpio.cleanup()
        


    def forward(self):
        """Go forward
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self._bl_pin, False)
        gpio.output(self._fl_pin, True)
        gpio.output(self._fr_pin, True)
        gpio.output(self._br_pin, False)
        
        
    def go_back(self):
        """Go back
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self._bl_pin, True)
        gpio.output(self._fl_pin, False)
        gpio.output(self._fr_pin, False)
        gpio.output(self._br_pin, True)
        time.sleep(sec)
        gpio.cleanup()
        
        
    def left_turn(self, sec):
        """Turn left
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self._bl_pin, True)
        gpio.output(self._fl_pin, False)
        gpio.output(self._fr_pin, True)
        gpio.output(self._br_pin, False)
        time.sleep(sec)
        gpio.cleanup()
        

    def right_turn(self, sec):
        """Turn right
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self._bl_pin, False)
        gpio.output(self._fl_pin, True)
        gpio.output(self._fr_pin, False)
        gpio.output(self._br_pin, True)
        time.sleep(sec)
        gpio.cleanup()        