#region Import
from machine import Pin, SoftI2C
import ssd1306
from neopixel import Neopixel
import time
import random

#endregion



#region Setup

# Set the pins
screen_pin = SoftI2C(scl=Pin(9), sda=Pin(8))

btn_A = Pin(15, Pin.IN, Pin.PULL_DOWN)
btn_B = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_C = Pin(13, Pin.IN, Pin.PULL_DOWN)
btn_D = Pin(12, Pin.IN, Pin.PULL_DOWN)
btn_E = Pin(3, Pin.IN, Pin.PULL_DOWN)
btn_list = [btn_A, btn_B, btn_C, btn_D, btn_E]

led_pin = 20

# Set up WS2812 LEDs
num_leds = 12
leds = Neopixel(num_leds, 0, led_pin)
leds.brightness(5)

led_A = 2
led_B = 4
led_C = 6
led_D = 8
led_E = 10
led_list = [led_A, led_B, led_C, led_D, led_E]

# Set color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color_list = [red, blue, green]

# Set the screen parameters
screen_width = 128
screen_height = 64
screen = ssd1306.SSD1306_I2C(screen_width, screen_height, screen_pin)

#endregion



#region Variables

patern = []

#endregion



#region Functions

def light_random(i):
    for x in range(i): 
        leds.clear()

        led_r = random.randrange(0, len(led_list))
        leds.set_pixel(led_list[led_r], blue)

        leds.show()

        time.sleep(0.5)

        leds.clear()
        leds.show()

        time.sleep(0.75)

#endregion



#region Exec

light_random(50)

#endregion
