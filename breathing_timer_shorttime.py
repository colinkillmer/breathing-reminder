from sense_hat import SenseHat
import time
import threading
from itertools import cycle

sense = SenseHat()
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

danger = [
  red,red,red,blue,blue,red,red,red,
  red,red,red,blue,blue,red,red,red,
  red,red,red,blue,blue,red,red,red,
  red,red,red,blue,blue,red,red,red,
  red,red,red,blue,blue,red,red,red,
  red,red,red,red,red,red,red,red,
  red,red,red,blue,blue,red,red,red,
  red,red,red,blue,blue,red,red,red
  ]


last_breath = time.time()

def breathing():
    global last_breath
    last_breath = time.time()

def alert_loop():
    while True:
        n = time.time() - last_breath # calculate elapsed time     
        if n>5 and n<=20:
            sense.show_message("Breathe!")
        elif n>20 and n<=30:
            sense.show_message("Now!!!", text_colour=blue, back_colour=white)
        elif n>30:
            sense.set_pixels(danger)
            time.sleep(.5)
            sense.clear()
            time.sleep(.5)

sense.stick.direction_any = breathing
alert_loop()
