const int relay = 26;// set the pin nuber according to your connection diagram
int incomingByte;      

void setup() {
  Serial.begin(115200);
  pinMode(relay, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(relay, LOW);
    }
    if (incomingByte == 'L') {
      digitalWrite(relay, HIGH);
    }    
  }
}
