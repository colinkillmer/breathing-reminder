from sense_hat import SenseHat
import time
import threading


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
    sense.clear()

 
def alert_loop():
    
    while True:
        n = time.time() - last_breath # calculate elapsed time     
        if n<1:
            sense.show_message("Cool", text_colour=green)
            sense.clear()
        elif n>305 and n<=320:
            sense.show_message("Breathe!")
            sense.clear()
        elif n>320 and n<=330:
            sense.show_message("Now!!!", text_colour=blue, back_colour=white)
            sense.clear()
        elif n>330:
            sense.set_pixels(danger)
            time.sleep(.5)
            sense.clear()
            time.sleep(.5)

sense.stick.direction_any = breathing
alert_loop()
