#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); //TX, RX
// (Send and Receive)

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {

  if(mySerial.available() > 0){//Read from  OSOYOO UART LoRa wireless module and send to serial monitor
    String input = mySerial.readString();
    Serial.println("Messsage received.");
    Serial.println(input);
  }
  
  if (Serial.available() > 1) { //Read from serial monitor and send over  OSOYOO UART LoRa wireless module
    String input = Serial.readString();
    mySerial.println(input);
    Serial.println("Messsage sent.");
    Serial.println(input);
  }

  delay(100);
}
