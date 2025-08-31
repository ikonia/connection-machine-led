# brought under git control to preseve code incase of loss
# everything under this comment is untouched from the original author
from machine import Pin, SPI
import max7219
import random
from time import sleep
spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 12 )
display.brightness(0)
while True:
   for y in range (8):
        for x in range (96):
            flip = random.randint(0, 1)
            if (flip == 0):
                flipp = random.randint(0, 1)   
                if (flipp == 0):
                    display.pixel(x,y,1)
                else:
                    display.pixel(x,y,0)
            else:
                pass
   display.show()
   timeflip = random.randint(0,3)
   if (timeflip == 0):
        sleep(1)
   elif (timeflip == 1):
        sleep(1.5)
   elif (timeflip == 2):
