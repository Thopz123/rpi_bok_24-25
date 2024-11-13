import machine
import utime
import urandom

# Setup for LED and buttons
led = machine.Pin(15, machine.Pin.OUT)
left_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

fastest_button = None

# Interrupt handler to determine the fastest button press
def button_handler(pin):
    global fastest_button
    fastest_button = pin
    # Disable further interrupts once a button is pressed
    left_button.irq(handler=None)
    right_button.irq(handler=None)

# Signal start of the game
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

# Enable interrupts for both buttons
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

# Wait for the fastest button press
while fastest_button is None:
    utime.sleep(1)

# Check which player pressed the button first
if fastest_button == left_button:
    print("Left Player Wins!")
elif fastest_button == right_button:
    print("Right Player Wins!")
