import RPi.GPIO as GPIO
import time

class servoRPi:
  def __init__(self, pin, Hz):
    self.servoPIN = pin
    self.Hz = Hz
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.servoPIN, GPIO.OUT)
    
  def servoFunc(self):
    p = GPIO.PWM(self.servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    try:
      while True:      
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
    except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()