# Import the library
from machine import Pin, SoftI2C
import ssd1306

# Set the pins
i2c = SoftI2C(scl=Pin(9), sda=Pin(8)) # Screen
btn = Pin(3, Pin.IN, Pin.PULL_DOWN) # Button

# Set the screen parameters
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Show the screen
oled.show()

while True :
    oled.fill(0)  # Clear the screen
    if btn.value() == 1:  # Button is pressed
        oled.text('Button Pressed!', 0, 0)
    else:
        oled.text('Press the button!', 0, 0)
    oled.show()
