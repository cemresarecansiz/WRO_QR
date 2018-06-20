#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  

  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

  

  Serial.println("Ready!");
}

void loop() {

  delay(100);
}

// callback for received data
void receiveData(int byteCount) {

  while (Wire.available()) {
    
    
    number = Wire.read();
    Serial.println(number);
    if (number == 1) {

      if (state == 0) {
        Serial.println("LED ON");
        state = 1;
      }
      else {
        Serial.println("LED OFF");
        state = 0;
      }
      
    }
  }
  
}

// callback for sending data
void sendData() {
  Wire.write(number);
  Serial.println("Sending...");
  Wire.begin(0x08);
  delay(100);

}
