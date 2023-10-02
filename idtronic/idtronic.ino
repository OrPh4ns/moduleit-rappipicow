/*
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.09.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W
@UHF    MetraTec
*/

const int buzzerPin = 5;
int volume = 1;
// 52 53 54 0D
const byte reset[] = {0x52, 0x53, 0x54, 0x0D};
// 53 54 44 20 45 54 53 0D
const byte ets[] = {0x53,0x54,0x44,0x20,0x45,0x54,0x53,0x0D};
// 53 52 49 20 4F 4E 0D
const byte sriOn[] = {0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E ,0x0D};
// 49 4E 56 0D
const byte inv[] = {0x49,0x4E,0x56,0x0D};

void setup()
{
  Serial1.setTimeout(10);
  // Start serial communication on Serial1 (TX1, RX0) at the desired baud rate
  Serial1.begin(115200); // Change the baud rate to match your sensor's specification
  Serial.begin(115200);
  Serial1.write(reset, sizeof(reset));
  Serial.println("Restting Reader ][ "+Serial1.readString()); 
  Serial1.write(ets, sizeof(ets));  
  Serial.println("STD ETS ][ "+Serial1.readString()); 
  Serial1.write(sriOn, sizeof(sriOn));  
  Serial.println("SRI ON ][ "+Serial1.readString()); 
}

void loop() 
{
  Serial1.println("49 4E 56 0D");
  if (Serial1.available())
  {
    String s = Serial1.readString();
    if(s.indexOf("NSS") != -1)
    {
      Serial.println("NSS => Selection of Standard");
      Serial1.write(ets, sizeof(ets));
      delay(500);
    }
    else if(s.indexOf("CRT") != -1)
    {
      Serial.println("CRT => Timeout or Failure");
      Serial1.write(reset, sizeof(reset));
      Serial.println("RST => Restting Reader ][ "+Serial1.readString()); 
      Serial1.write(ets, sizeof(ets));  
      Serial.println("RST => STD ETS ][ "+Serial1.readString()); 
      Serial1.write(sriOn, sizeof(sriOn));  
    }
    else 
    Serial.println(s);
  }
  else
  {
    Serial1.write(inv, sizeof(inv));
  }
}
