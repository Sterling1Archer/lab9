#include <Servo.h>
Servo top_servo;
Servo bottom_servo;

void setup(){
  Serial.begin(9600);
  top_servo.attach(5);
  top_servo.attach(6);
}

void loop(){
  int top_angle;
  int bottom_angle;
  int motor_ID,motor_angle;
  
  if (Serial.available())  {
    motor_ID = Serial.parseInt();
    Serial.println("motor_ID: ");
    Serial.println(motor_ID);
    motor_angle = Serial.parseInt();
    Serial.println("motor_angle: ");
    Serial.println(motor_angle);
    switch(motor_ID){
      case 0: top_angle = motor_angle; break;
      case 1: bottom_angle = motor_angle; break;
    }
    top_servo.write(top_angle);
    bottom_servo.write(bottom_angle);
    delay(1000);
  }
}
