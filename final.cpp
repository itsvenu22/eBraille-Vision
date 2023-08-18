#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

#define LED_PIN_1 13
#define LED_PIN_2 12
#define LED_PIN_3 8
#define LED_PIN_4 7
#define LED_PIN_5 4
#define LED_PIN_6 2

#define SERVO_PIN_1 11
#define SERVO_PIN_2 10
#define SERVO_PIN_3 9
#define SERVO_PIN_4 6
#define SERVO_PIN_5 5
#define SERVO_PIN_6 3



void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(ledPin5, OUTPUT);
  pinMode(ledPin6, OUTPUT);

  servo1.attach(servoPin1);
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);

  
  offed();
}

void loop() {
  String inputStr;
  
  Serial.println("Enter data: ");
  while (Serial.available() == 0) {

  }
  
  inputStr = Serial.readStringUntil('\n');
  
  for (int i = 0; i < inputStr.length(); i++) {
    char c = inputStr.charAt(i);
    
    if (data.containsKey(c)) {
      int ledIndex = data[c][0][0];
      int ledPin = led_pin[ledIndex][data[c][0][1]];
      int servoIndex = data[c][0][0];
      int servoPin = servo_pin[servoIndex][data[c][0][1]];
      
      digitalWrite(ledPin, HIGH);
      sev0(servoPin);
      delay(3000);
      digitalWrite(ledPin, LOW);
    }
  }
}

void offed() {
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
  digitalWrite(ledPin5, LOW);
  digitalWrite(ledPin6, LOW);
}

void sev0(int k) {
  int servoPin;
  Servo servo;
  
  switch (k) {
    case 17:
      servoPin = servoPin1;
      servo = servo1;
      break;
    case 18:
      servoPin = servoPin2;
      servo = servo2;
      break;
    case 27:
      servoPin = servoPin3;
      servo = servo3;
      break;
 
  }
  
  servo.attach(servoPin);
  servo.write(45);
  delay(1000);
  servo.detach();
}
