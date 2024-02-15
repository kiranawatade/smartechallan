
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);
#define ir 2
#define r 3
#define buz 4
#define sw 5
#define re 6
#define ye 7
#define ge 8
int a,b,c;
void setup() 
{
  Serial.begin(9600); 
   lcd.begin();

  // Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Smart E-Challan");
  
  lcd.setCursor(3,1);
  lcd.print("For Smart City");
  delay(2000);
  lcd.clear();
  pinMode(ir,INPUT);
  
  pinMode(sw,INPUT);
  pinMode(r,OUTPUT);
  
  pinMode(buz,OUTPUT);
   pinMode(re,OUTPUT);
    pinMode(ye,OUTPUT);
     pinMode(ge,OUTPUT);
  digitalWrite(r,1);
  digitalWrite(buz,0);
  
  digitalWrite(re,0);
  
  digitalWrite(ye,0);

  
  digitalWrite(ge,0);
  
  
}
void loop() 
{
 
  lcd.setCursor(0,0);
  lcd.print("Smart E-Challan");
  
  lcd.setCursor(3,1);
  lcd.print("For Smart City");
  delay(500);
  lcd.clear();
  a=digitalRead(ir);
   b=digitalRead(sw);
   if(b==1)
   {
      digitalWrite(ye,0);
   
   digitalWrite(ge,0);
   
  
   digitalWrite(re,1);
   
   digitalWrite(r,0);
  if(a==1)
  {
    SendMessage();  
     
    SendMessage1(); 
   digitalWrite(buz,1);
   delay(1000);
   digitalWrite(buz,0);
      delay(1000);
  }
   if(a==0)
  {
   Serial.print("nort");
   digitalWrite(buz,0);
  }
   }
  if(b==0)
   {
    digitalWrite(buz,0);
   digitalWrite(ye,1);
   
   digitalWrite(ge,0);
   
   digitalWrite(re,0);
   
   digitalWrite(r,1);
   delay(2000);
  digitalWrite(buz,0);
   digitalWrite(ye,0);
   
   digitalWrite(ge,1);
   
   digitalWrite(re,0);
   
   digitalWrite(r,1);
 delay(2000);
   }
  
}

 void SendMessage()      
{
  lcd.clear();
   lcd.setCursor(0,0);
  lcd.print("  ALERT  ");
  lcd.setCursor(0,1);
  lcd.print("VIOLATION DETECTED");
  delay(2000);
  Serial.println("AT+CMGF=1");    // sending command code
  delay(1000);  

  Serial.println("AT+CMGS=\"+919284161989\"\r"); // Replace * with mobile number

  delay(1000);

  
  Serial.print("  ALERT  ");
  
  Serial.println("       ");

  Serial.println("Your fine amount of 299 leived for Traffic Violation Pay to Aviod Auto Debit"); // The SMS text you want to send


  Serial.println("       ");
  
  Serial.println("       ");

//
  delay(100);

  Serial.println((char)26);
  delay(1000);
  lcd.clear();
  lcd.print("SMS SENT");
  delay(1000);
}

  void SendMessage1()      
{
  lcd.clear();
   lcd.setCursor(0,0);
  lcd.print("  ALERT  ");
  lcd.setCursor(0,1);
  lcd.print("VIOLATION DETECTED");
  delay(2000);
  Serial.println("AT+CMGF=1");    // sending command code
  delay(1000);  

  Serial.println("AT+CMGS=\"+918087114548\"\r"); // Replace * with mobile number

  delay(1000);

  
  Serial.print("  ALERT  ");
  
  Serial.println("       ");

  Serial.println("Your fine amount of 299 leived for Traffic Violation Pay to Aviod Auto Debit"); // The SMS text you want to send


  Serial.println("       ");
  
  Serial.println("       ");

//
  delay(100);

  Serial.println((char)26);
  delay(1000);
  lcd.clear();
  lcd.print("SMS SENT");
  delay(1000);
}
