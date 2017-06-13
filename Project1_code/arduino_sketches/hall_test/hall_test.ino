int hall = 5;

void setup() {
  Serial.begin(9600);
  pinMode(hall, INPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(digitalRead(hall));
}
