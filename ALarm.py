import machine
import utime

# Set up PIR sensor, LED, and buzzer
sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

# Interrupt handler for motion detection
def pir_handler(pin):
    print("ALARM! Motion detected!")
    for i in range(50):
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)

# Attach the interrupt handler to the PIR sensor for rising edge detection
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

# Main loop
while True:
    led.toggle()
    utime.sleep(5)

