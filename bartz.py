from sense_hat import SenseHat
import time

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

def breathing():
    sense.show_message("cool")
    time.sleep(1)
    n=0
    while True:
        if n<5:
            sense.show_message("Breathe!")
            n=n+1
        elif n<10:
            sense.show_message("NOW!!!", text_colour=blue, back_colour=white)
            n=n+1
        else:
            sense.set_pixels(danger)
            time.sleep(.5)
            sense.clear()
            time.sleep(.5)
sense.stick.direction_any = breathing
while True:
    pass
