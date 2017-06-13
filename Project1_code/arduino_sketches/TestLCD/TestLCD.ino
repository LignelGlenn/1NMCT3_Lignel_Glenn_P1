//int RSPin = 3;
//int EPin = 5;
//int DP4 = 6;
//int DP5 = 7;
//int DP6 = 8;
//int DP7 = 9;
#include <LiquidCrystal.h>
//RS E DP4, 5, 6, 7
LiquidCrystal lcd(3, 5, 6, 7, 8, 9);
void setup() {
  //pinMode(RSPin, OUTPUT);
  //pinMode(RWPin, OUTPUT);
  //pinMode(EPin, OUTPUT);
  //pinMode(DP4, OUTPUT);
  //pinMode(DP5, OUTPUT);
  //pinMode(DP6, OUTPUT);
  //pinMode(DP7, OUTPUT);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  //lcd.clear();
  //lcd.setCursor(0, 0);
  lcd.print("hello");
  delay(1000);
}

