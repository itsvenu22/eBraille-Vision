import RPi.GPIO as GPIO
import time
import os

def offed():
    pins_to_off = [17, 18, 27, 22, 23, 21]
    GPIO.setmode(GPIO.BCM)
    for pin in pins_to_off:
        GPIO.output(pin, GPIO.LOW)

def sev0(k):

    servo_pin = k
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(0)

    def set_angle(angle):
        duty = angle / 18 + 2
        GPIO.output(servo_pin, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(servo_pin, False)
        #pwm.ChangeDutyCycle(0)
    try:

        set_angle(45)
        #time.sleep(3)
        #set_angle(0)
    finally:
        pwm.stop()
        GPIO.cleanup()

k=input()
sev0(k)
