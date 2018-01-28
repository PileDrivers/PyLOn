#include <Servo.h>

int motorA = 12;
int motorB = 13;

void setup() {
 // initialize the digital pins as an output
  pinMode ( motorA, OUTPUT);
  pinMode ( motorB, OUTPUT);

// Turn the Serial Protocol ON
 Serial.begin(9600);
}

void loop() {
 byte byteRead1;


 /* check if data has been sent from the computer: */
 if (Serial.available()) {

 /* read the most recent byte */
 byteRead1 = Serial.read();
 Serial.print(byteRead1);

 //You have to subtract '0' from the read Byte to convert from text to a number.

 //case you want to go forward
 if (byteRead1 == '1'){
  digitalWrite( motorA, HIGH);
  digitalWrite( motorB, HIGH);
  delay(1000);
  digitalWrite( motorA, LOW);
  digitalWrite( motorB, LOW);
 }

 //case you want to go right
 else if (byteRead1 == '2'){
  digitalWrite( motorA, HIGH);
  digitalWrite( motorB, LOW);
  delay(1000);
  digitalWrite( motorA, LOW);
  digitalWrite( motorB, LOW);
 }

 //case you want to go left
 else if (byteRead1 == '3'){
  digitalWrite( motorA, LOW);
  digitalWrite( motorB, HIGH);
  delay(1000);
  digitalWrite( motorA, LOW);
  digitalWrite( motorB, LOW);
 }

 //otherwise
 else {
  digitalWrite( motorA, LOW);
  digitalWrite( motorB, LOW);
 }


 }
 }
