int ledRedPin = 2;
int ledGreenPin = 3;
int ledStatus;
int incomingByte = 0;
int buzzerPort = 4;



void setup(){
  pinMode(ledRedPin, OUTPUT);
  pinMode(ledGreenPin, OUTPUT);
  Serial.begin(9600);

}


void loop(){

  if(Serial.available() > 0 ){
    incomingByte = Serial.read();
  }

  if( incomingByte == 48 ){
    digitalWrite(ledRedPin, HIGH);
  }
  else{
    digitalWrite(ledRedPin, LOW);
  }

  if( incomingByte == 50 ){
    digitalWrite(ledGreenPin, HIGH);
  }
  else{
    digitalWrite(ledGreenPin, LOW);
  }
  
  if( incomingByte == 52 ){
    //digitalWrite(ledGreenPin, HIGH);
    buzzer();
  }

}


void buzzer(){
  int melodia[] = { 660, 660, 660, 510, 660, 770, 380, 320, 440, 480, 450, 430, 380 };
  int duracaoDasNotas[] = {100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 80, 100, 100, 50, 100};
  
  for(int nota = 0; nota < 16; nota++){
     int duracaoDaNota = duracaoDasNotas[nota];
     tone(buzzerPort, melodia[nota], duracaoDaNota);
     int pausaDepoisDasNotas[] = { 150, 300, 300, 100, 300, 550, 575, 450, 400, 500, 300, 330, 150, 300, 200, 200 };
  
     delay(pausaDepoisDasNotas[nota]);
     noTone(buzzerPort); 
  }
  
}


