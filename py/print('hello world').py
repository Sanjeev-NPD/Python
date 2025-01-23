#include <LiquidCrystal_I2C.h>
int totalColumns = 16;
int totalRows = 2;

 LiquidCrystal_I2C lcd(0x27, totalColumns, totalRows);

   const int stepPin1 = A1;
   const int dirPin1 = A2;
   const int stepPin2 = A0;
   const int dirPin2 = A3;
   const int bt_F = 7; 
   const int bt_S = 8;
   const int bt_B = 9; 

   int count;
   float delay_time=500;
   int buttonState1 = 0;
   int buttonState2 = 0;
   int buttonState3 = 0;

    void setup()
   {
    Serial.begin(115200);
    pinMode(stepPin1,OUTPUT); 
    pinMode(dirPin1,OUTPUT);
    pinMode(stepPin2,OUTPUT); 
    pinMode(dirPin2,OUTPUT);
    pinMode(bt_F,INPUT);
    pinMode(bt_S,INPUT);
    pinMode(bt_B,INPUT);

    lcd.init(); 
    lcd.backlight();
    lcd.clear();
    count = 0;
    delay(2000);        
    lcd.setCursor(0,0);             
    lcd.print("Coil Winding");
    lcd.setCursor(0,0); 
//    lcd.print("COIL TURNS = ");
//    lcd.print(count);
    delay(2000);
   }

  void loop() 
{  
     count++;
    lcd.setCursor(0,0); 
    lcd.print("COIL TURNS = ");
    lcd.print(count);
    buttonState1 = digitalRead(bt_F);
    Serial.print("lelo maja");
    Serial.print(buttonState1);
    if (buttonState1 = HIGH)
    {
       digitalWrite(dirPin1,HIGH);
       digitalWrite(dirPin2,HIGH);
  for(int x = 0; x<200; x++)
      { 
  digitalWrite(stepPin1,HIGH);
  digitalWrite(stepPin2,HIGH);
  delayMicroseconds(500);
  digitalWrite(stepPin1,LOW);
  digitalWrite(stepPin2,LOW); 
  delayMicroseconds(500);
  delay(3);
           }
      }
      else
      {
       digitalWrite(dirPin1,LOW);
       digitalWrite(dirPin2,LOW);
  for(int x = 0; x<200; x++)
      { 
  digitalWrite(stepPin1,HIGH);
  digitalWrite(stepPin2,HIGH);
  delayMicroseconds(500);
  digitalWrite(stepPin1,LOW);
  digitalWrite(stepPin2,LOW); 
  delayMicroseconds(500);
  delay(3);
  
      }
      }

     buttonState2 = digitalRead(bt_S);
     if(buttonState2 = LOW)
     {
      while(1);
      }
}
     

