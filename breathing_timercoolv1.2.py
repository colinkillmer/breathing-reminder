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
        elif n>30 and n<=40:
            sense.show_message("Breathe...", text_colour=blue)
            sense.clear()
        elif n>40 <=44:
            sense.clear((255,255,204))
            time.sleep(.4)
        elif n>=44 and n<=51:
            sense.clear((255,204,255))
            time.sleep(1.7)
        elif n>51 and n<59:
            sense.clear((153,255,153))
            time.sleep(.625)
            n=n+.625
        elif n>=59:
            n=time.time()+ last_breath
        
                  

sense.stick.direction_any = breathing
alert_loop()
