# Import the libraries
from machine import Pin, SoftI2C
import ssd1306
from neopixel import Neopixel

# Set the pins
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))  # Screen
btn_A = Pin(15, Pin.IN, Pin.PULL_DOWN)  # Button
btn_B = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Button
btn_C = Pin(13, Pin.IN, Pin.PULL_DOWN)  # Button
btn_D = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Button
btn_E = Pin(3, Pin.IN, Pin.PULL_DOWN)   # Button

# Set up WS2812 LEDs
num_leds = 12  # Number of LEDs in the ring
led_pin = 20  # Pin connected to the data line of the LED ring
leds = Neopixel(num_leds,0,led_pin)
leds.brightness(5)

# Set the screen parameters
screen_width = 128
screen_height = 64
screen = ssd1306.SSD1306_I2C(screen_width, screen_height, i2c)

# Function to light up the first LED
def light_up_first_led(color):
    leds.fill((0, 0, 0))
    leds.set_pixel(0,color)
    leds.show()

# Main loop
while True:
    screen.fill(0)  # Clear the screen

    if btn_A.value() == 1:  # Button is pressed
        screen.text('Button A Pressed!', 0, 0)
        light_up_first_led((255, 0, 0))  # Light up the first LED in red
    elif btn_B.value() == 1:  # Button is pressed
        screen.text('Button B Pressed!', 0, 0)
        light_up_first_led((0, 255, 0))  # Light up the first LED in green
    elif btn_C.value() == 1:  # Button is pressed
        screen.text('Button C Pressed!', 0, 0)
        light_up_first_led((0, 0, 255))  # Light up the first LED in blue
    elif btn_D.value() == 1:  # Button is pressed
        screen.text('Button D Pressed!', 0, 0)
        light_up_first_led((255, 255, 0))  # Light up the first LED in yellow
    elif btn_E.value() == 1:  # Button is pressed
        screen.text('Button E Pressed!', 0, 0)
        light_up_first_led((255, 0, 255))  # Light up the first LED in purple
    else:
        screen.text('Press the button!', 0, 0)
        light_up_first_led((0, 0, 0))  # Turn off all LEDs

    screen.show()

