# GPIO library
import Jetson.GPIO as GPIO
 
# Handles time
import time 
 
# Pin Definition
led_pin = 7
 
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)
 
print("Press CTRL+C when you want the LED to stop blinking") 

# Blink the LED
while True: 
  time.sleep(2) 
  GPIO.output(led_pin, GPIO.HIGH) 
  print("LED is ON")
  time.sleep(2) 
  GPIO.output(led_pin, GPIO.LOW)
  print("LED is OFF")