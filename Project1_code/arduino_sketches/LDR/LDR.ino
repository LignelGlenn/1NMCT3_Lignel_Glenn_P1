int ldr = A1;
int ldrWaarde = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  ldrWaarde = analogRead(ldr);
  Serial.println("De digitale waarde over de trimmer is: " + String(ldrWaarde));
  Serial.println("De lichtwaarde bedraagt: " + String(berekenSpanningLdr(ldrWaarde)) + "%");
}

float berekenSpanningLdr(int ldrWaarde){
  float procent =100-(ldrWaarde/1023.0*100);
  return procent;
}
