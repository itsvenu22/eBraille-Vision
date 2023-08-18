import RPi.GPIO as GPIO
import time
import os

def offed():
    pins_to_off = [17, 18, 27, 22, 23, 21]
    GPIO.setmode(GPIO.BCM)
    for pin in pins_to_off:
        GPIO.output(pin, GPIO.LOW)

'''
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
'''

data = {'A':[[0,0]],
        'B':[[0,0],[1,0]],
        'C':[[0,0],[0,1]],
        'D':[[0,0],[0,1],[1,1]],
        'E':[[0,0],[1,1]],
        'F':[[0,0],[0,1],[1,0]],
        'G':[[0,0],[0,1],[1,0],[1,1]],
        'H':[[0,0],[1,0],[1,1]],
        'I':[[0,1],[1,0]],
        'J':[[0,1],[1,0],[1,1]],
        'K':[[0,0],[2,0]],
        'L':[[0,0],[1,0],[2,0]],
        'M':[[0,0],[0,1],[2,0]],
        'N':[[0,0],[0,1],[1,1],[2,0]],
        'O':[[0,0],[1,1],[2,0]],
        'P':[[0,0],[0,1],[1,0],[2,0]],
        'Q':[[0,0],[0,1],[1,0],[1,1],[2,0]],
        'R':[[0,0],[1,0],[1,1],[2,0]],
        'S':[[0,1],[1,0],[2,0]],
        'T':[[0,1],[1,0],[1,1],[2,0]],
        'U':[[0,0],[2,0],[2,1]],
        'V':[[0,0],[1,0],[2,0],[2,1]],
        'W':[[0,1],[1,0],[1,1],[2,1]],
        'X':[[0,0],[0,1],[2,0],[2,1]],
        'Y':[[0,0],[0,1],[1,1],[2,0],[2,1]],
        'Z':[[0,0],[1,1],[2,0],[2,1]]
}


servo_pin = [[5,12],[6,13],[19,26]]
led_pin = [[17,18],[27,22],[23,21]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


try:
    offed()
    while (True):
        str = input("Enter data : ")
        for i in str:
            l1 = data[i]
            led = []
            #serv0=[]
            for i in range(len(l1)):
                led.append(led_pin[l1[i][0]][l1[i][1]])
                #serv0.append(servo_pin[l1[i][0]][l1[i][1]])

            for i in led:
                GPIO.output(i, GPIO.HIGH)  
            #for i in serv0:
                #sev0(i)
            time.sleep(3)
            for i in led:
                GPIO.output(i, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
