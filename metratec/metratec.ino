/*
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.09.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W
@UHF    MetraTec
*/

#define RD 0x28;
const byte read_f[] = {0x52, 0x02};

void setup()
{
  Serial1.setTimeout(10);
  Serial1.begin(115200); // Change the baud rate to match your sensor's specification
  Serial.begin(115200);
  Serial.println("Restting Reader ][ "+Serial1.readString()); 
  Serial.println("STD ETS ][ "+Serial1.readString()); 
}

void loop()
{
  //Serial1.write(read_f, sizeof(read_f));
  Serial1.write(0x28);
  Serial.println(Serial1.readString());
  //if (Serial1.available())
  //{
  //}
  delay(500);
  //Serial.println(MSG_CRC_INIT);
}
