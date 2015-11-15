int ledRedPin = 2;
int ledGreenPin = 3;
int ledStatus;




void setup(){
  pinMode(ledRedPin, OUTPUT);
  pinMode(ledGreenPin, OUTPUT);
  Serial.begin(9600);
  
}


void loop(){

  if(Serial.available() > 0){
    ledStatus = Serial.parseInt();
    digitalWrite(ledRedPin, ledStatus);
  }
  
}

