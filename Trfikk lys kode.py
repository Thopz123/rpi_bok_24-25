import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

button_pressed = False
lock = _thread.allocate_lock()

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            with lock:
                button_pressed = True
            utime.sleep(0.1)  # Debounce delay
        utime.sleep(0.01)  # Polling delay

_thread.start_new_thread(button_reader_thread, ())

def activate_buzzer():
    for _ in range(10):
        buzzer.value(1)
        utime.sleep(0.2)
        buzzer.value(0)
        utime.sleep(0.2)

def traffic_light_sequence():
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)

while True:
    if button_pressed:
        with lock:
            button_pressed = False
        led_red.value(1)
        activate_buzzer()
    
    traffic_light_sequence()
