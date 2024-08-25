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
            bl_pin (int): back left pin;   if this pin is true, left motor would be to back.
            fl_pin (int): front left pin;  if this pin is true, left motor would be to front.
            br_pin (int): back right pin;  if this pin is true, right motor would be to back.
            fr_pin (int): front right pin; if this pin is true, right motor would be to front.
        """
        
        # setup motor pins
        self.bl_pin = bl_pin
        self.fl_pin = fl_pin
        self.br_pin = br_pin
        self.fr_pin = fr_pin
        
    
    def reset_pin(self):
        """Reset pin setting to OUT"""
        gpio.setmode(gpio.BCM) # set the pin style BCM
        gpio.setup(self.bl_pin, gpio.OUT) # back left pin
        gpio.setup(self.fl_pin, gpio.OUT) # front left pin
        gpio.setup(self.fr_pin, gpio.OUT) # front right pin
        gpio.setup(self.br_pin, gpio.OUT) # back right pin


    def forward(self, sec):
        """Go forward
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self.bl_pin, False)
        gpio.output(self.fl_pin, True)
        gpio.output(self.fr_pin, True)
        gpio.output(self.br_pin, False)
        time.sleep(sec)
        gpio.cleanup() 
        
        
    def go_back(self, sec):
        """Go back
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self.bl_pin, True)
        gpio.output(self.fl_pin, False)
        gpio.output(self.fr_pin, False)
        gpio.output(self.br_pin, True)
        time.sleep(sec)
        gpio.cleanup()
        
        
    def left_turn(self, sec):
        """Turn left
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self.bl_pin, True)
        gpio.output(self.fl_pin, False)
        gpio.output(self.fr_pin, True)
        gpio.output(self.br_pin, False)
        time.sleep(sec)
        gpio.cleanup()
        
        
    def right_turn(self, sec):
        """Turn right
        
        Args:
            sec (int): moving time.
        """
        gpio.output(self.bl_pin, False)
        gpio.output(self.fl_pin, True)
        gpio.output(self.fr_pin, False)
        gpio.output(self.br_pin, True)
        time.sleep(sec)
        gpio.cleanup()


if __name__=="__main__":
    controller = Controller(17, 22, 24, 23)