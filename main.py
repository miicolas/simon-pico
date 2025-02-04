#region Import
from machine import Pin, SoftI2C
import ssd1306
from neopixel import Neopixel
import time
import random
#endregion

#region Constants
# Pins
SCL_PIN = 9
SDA_PIN = 8
BTN_PINS = [15, 14, 13, 12, 3]  # A, B, C, D, E
LED_PIN = 20

# Display
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# LED Configuration
NUM_LEDS = 12
LED_INDICES = [2, 4, 6, 8, 10]  # Corresponding to buttons A-E
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'off': (0, 0, 0)
}

# Game Settings
INITIAL_CHAIN = 1
PATTERN_DELAY = 500  # milliseconds
#endregion

#region Hardware Setup
# Initialize Screen
i2c = SoftI2C(scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))
screen = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

# Initialize Buttons
buttons = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in BTN_PINS]

# Initialize LEDs
leds = Neopixel(NUM_LEDS, 0, LED_PIN)
leds.brightness(5)
#endregion

#region Game State
best_score = 0
current_score = 0
pattern = []
chain_length = INITIAL_CHAIN
#endregion

#region Helper Functions
def show_start_screen():
    screen.fill(0)
    screen.text(f'Best: {best_score}', 0, 0)
    screen.text(f'Last: {current_score}', 0, 10)
    screen.text('Press any button', 0, 30)
    screen.text('to START!', 0, 40)
    screen.show()

def generate_pattern(length):
    return [random.randint(0, len(buttons)-1) for _ in range(length)]

def display_pattern(pattern):
    for led_index in pattern:
        leds.set_pixel(LED_INDICES[led_index], COLORS['blue'])
        leds.show()
        time.sleep_ms(PATTERN_DELAY)
        leds.set_pixel(LED_INDICES[led_index], COLORS['off'])
        leds.show()
        time.sleep_ms(PATTERN_DELAY//2)

def wait_for_button(timeout=5000):
    start_time = time.ticks_ms()
    while True:
        for i, btn in enumerate(buttons):
            if btn.value():
                # Debounce
                time.sleep_ms(20)
                while btn.value():
                    pass
                return i
        if time.ticks_diff(time.ticks_ms(), start_time) > timeout:
            return None

def check_pattern(expected_pattern):
    for expected in expected_pattern:
        pressed = wait_for_button()
        if pressed is None or pressed != expected:
            # Incorrect or timeout
            leds.set_pixel(LED_INDICES[pressed], COLORS['red'])
            leds.show()
            time.sleep(1)
            leds.set_pixel(LED_INDICES[pressed], COLORS['off'])
            leds.show()
            return False
        # Visual feedback for correct press
        leds.set_pixel(LED_INDICES[pressed], COLORS['green'])
        leds.show()
        time.sleep(0.2)
        leds.set_pixel(LED_INDICES[pressed], COLORS['off'])
        leds.show()
    return True

def game_over():
    global best_score
    if current_score > best_score:
        best_score = current_score
    show_start_screen()
#endregion

#region Main Game Loop
while True:
    show_start_screen()
    
    # Wait for any button press to start
    while not any(btn.value() for btn in buttons):
        pass
    
    # Initialize game
    current_score = 0
    chain_length = INITIAL_CHAIN
    
    while True:
        # Generate and show pattern
        pattern = generate_pattern(chain_length)
        display_pattern(pattern)
        
        # Check user input
        if check_pattern(pattern):
            current_score += chain_length
            chain_length += 1
        else:
            break
    
    # Handle game over
    game_over()
#endregion