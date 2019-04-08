#This section imports libraries of terms used by the program
import unicornhathd as unicorn
import time
import colorsys
import threading
from gpiozero import Button
from PIL import Image, ImageDraw, ImageFont

#This part tells the program to get the width and height of the display from the device
width, height = unicorn.get_shape()

#This section defines common color variables that can used by the entire program
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)




#This is used to define time zero, when the last breath occurred
last_breath = time.time()

#To change what text scrolls across, change the words in lines and reminders.
lines = ["cool...",]
reminders = ["breathe"]

colours = [green, blue, white, red]

#To change the font used and its size, edit this part to pick from a font saved in the folder.
FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 12)

#This part defines what to set as true when the button is pressed
def breathing():
    global last_breath
    last_breath = time.time()
    unicorn.clear()

#This part of the program indicates what happens after the button is pressed, and is part of the timer system called alert loop
def alert_loop():
    
    while True:
        n = time.time() - last_breath # calculate elapsed time in seconds
        #from here on, n refers to seconds passed. Change what n equals, is greater than, or less than to alter times.
#while less than 1 second has occurred, scroll through the text defined by the lines section above.
        if n<1:
            unicorn.brightness(.8)
            text_x = width
            text_y = 2
            font_file, font_size = FONT
            font = ImageFont.truetype(font_file, font_size)
            text_width, text_height = width, 0
            for line in lines:
                w, h = font.getsize(line)
                text_width += w + width
                text_height = max(text_height, h)
            text_width += width + text_x +1

            image = Image.new('RGB', (text_width, max(16, text_height)), nothing)
            draw = ImageDraw.Draw(image)

            offset_left = 0

            for index, line in enumerate(lines):
                draw.text((text_x + offset_left, text_y), line, green, font=font)
                offset_left += font.getsize(line)[0] + width
            for scroll in range(text_width - width):
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel((x + scroll, y))
                        r,g,b = [int(n) for n in pixel]
                        unicorn.set_pixel(width - 1 -x, y, r,g,b)
                unicorn.show()
                time.sleep(0.02)
#when 5 minutes have passed, scroll through the text defined by the reminders section above until 7 minutes have passed
        elif n>30 and n<=60:
            unicorn.brightness(.8)
            text_x = width
            text_y = 2
            font_file, font_size = FONT
            font = ImageFont.truetype(font_file, font_size)
            text_width, text_height = width, 0
            for reminder in reminders:
                w, h = font.getsize(reminder)
                text_width += w + width
                text_height = max(text_height, h)
            text_width += width + text_x +1

            image = Image.new('RGB', (text_width, max(16, text_height)), nothing)
            draw = ImageDraw.Draw(image)

            offset_left = 0

            for index, reminder in enumerate(reminders):
                draw.text((text_x + offset_left, text_y), reminder, blue, font=font)
                offset_left += font.getsize(line)[0] + width
            for scroll in range(text_width - width):
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel((x + scroll, y))
                        r,g,b = [int(n) for n in pixel]
                        unicorn.set_pixel(width - 1 -x, y, r,g,b)
                unicorn.show()
                time.sleep(0.02)
#after 7 minutes have passed, 4,7,8 breathing cycle begins
        elif n>60:
            b=0
            p=0
            while True:
                if p<4:
                    unicorn.brightness(b)
                    unicorn.set_all(255,255,255)
                    time.sleep(.4)
                    unicorn.show()
                    b=b+.1
                    p=p+0.4
                elif p>=4 and p<=11:
                    b=1
                    unicorn.brightness(b)
                    unicorn.set_all(255,255,255)
                    unicorn.show()
                    time.sleep(1.7)
                    p=p+1.7
                elif p>11:
                    unicorn.brightness(b)
                    unicorn.set_all(255,255,255)
                    unicorn.show()
                    time.sleep(.625)
                    b=b-0.1
                    p=p+.625
                    if p>=19:
                        p=0
                  
                
                    
       
alert_loop()
